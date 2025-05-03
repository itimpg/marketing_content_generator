from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain_core.output_parsers import StrOutputParser

# Load environment variables if needed
load_dotenv()

# Initialize LangChain components
base_url = "http://localhost:11434"
model = "llama3.2"
llm = ChatOllama(base_url=base_url, model=model)

# Define prompts
system = SystemMessagePromptTemplate.from_template('You are the Marketing Manager of Manao Software, a modern and innovative software development company. Your job is to create clear, engaging, and friendly content for Facebook that explains technical topics in simple terms for non-technical audiences. You use a casual yet professional tone, and highlight the company’s values of collaboration, flexibility, and innovation.')
human = HumanMessagePromptTemplate.from_template('Write a friendly and easy-to-understand Facebook post for a company fan page, explaining the topic of {topic} to a non-technical audience. Keep the tone casual and engaging, highlight how it benefits customers or the team, and use short paragraphs or bullet points. Limit the content to a format suitable for a social media post.')
facebook_post_prompt = ChatPromptTemplate.from_messages([system, human])
facebook_post_chain = facebook_post_prompt | llm | StrOutputParser()

video_script_prompt = ChatPromptTemplate.from_template('''
    Use the following context: {context} to write a script for a 1-minute video. 
    The script should be clear, engaging, and easy to understand for a non-technical audience. 
    Maintain a friendly, conversational tone and avoid jargon. 
    Focus on delivering one key message or takeaway, with a hook at the beginning to grab attention.
    Make sure the script fits a vertical social media video format and encourages viewer interaction or shares.
''')
video_script_chain = video_script_prompt | llm | StrOutputParser()

# Define input schema
class MarketingRequest(BaseModel):
    topic: str

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Be specific in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/marketing-content")
async def generate_marketing_content(req: MarketingRequest):
    try:
        facebook_post = facebook_post_chain.invoke({'topic': req.topic})
        video_script = video_script_chain.invoke({'context': facebook_post})

        return JSONResponse(content={
            "facebook_post": facebook_post,
            "video_script": video_script
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
