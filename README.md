# Marketing Content Generator

This project generates marketing content such as Facebook posts and video scripts based on a given topic. It exposes a FastAPI backend with an endpoint that accepts a topic and returns generated content for the topic. The frontend allows users to enter a topic, generate the content, and view the results in a tabbed interface with a loading spinner during the request.

## Features

- **API Endpoint**: A FastAPI server that accepts a POST request at `/marketing-content` with a `topic` and returns a generated Facebook post and video script.
- **Frontend Interface**: A simple web page with a text input to enter the topic, a button to generate the content, and a tabbed interface to display the results (Facebook post and video script).
- **Loading Spinner**: A spinner is shown while the API request is in progress and hidden once the content is received.

## Technologies Used

- **Backend**:
  - FastAPI (Python)
  - Pydantic (for request validation)
  
- **Frontend**:
  - HTML
  - CSS
  - JavaScript (Vanilla)
  
- **Other**:
  - Fetch API for making HTTP requests from frontend to backend

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/marketing-content-generator.git
cd marketing-content-generator
```

### 2. Backend Setup (FastAPI)

#### Install Python dependencies

Ensure you have Python 3.8+ installed. You can create a virtual environment and install the required dependencies using `pip`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the FastAPI Backend

Make sure your backend code (FastAPI server) is ready, then run it with the following command:

```bash
uvicorn main:app --reload
```

This will start the backend server on `http://localhost:8000`.

### 3. Frontend Setup

The frontend is a static `index.html` file, which does not require any server-side processing. You can simply open the `index.html` file in a web browser. Alternatively, you can serve it using a simple HTTP server:

#### Serve via Python (optional):

```bash
python -m http.server
```

This will serve the frontend at `http://localhost:8000`, but you can also open the `index.html` file directly in any browser.

### 4. Test the Application

1. Open the `index.html` file in your browser.
2. Enter a topic (e.g., "Agile Methodology") in the input field.
3. Click **Generate** to see the generated **Facebook Post** and **Video Script** in the respective tabs.
4. You should see a loading spinner while the content is being fetched.

## Project Structure

```
marketing-content-generator/
│
├── backend/                # FastAPI backend
│   ├── main.py             # FastAPI app and routes
│   ├── requirements.txt    # Backend dependencies
│
├── frontend/               # Frontend files
│   └── index.html          # Main HTML file for the frontend
├── README.md               # Project documentation
```

## API Documentation

### POST `/marketing-content`

- **Request Body**:
  - `topic` (string): The topic for which to generate marketing content (e.g., "Agile Methodology").
  
  Example Request:
  ```json
  {
    "topic": "Agile Methodology"
  }
  ```

- **Response**:
  - `facebook_post` (string): The generated Facebook post content.
  - `video_script` (string): The generated video script content.

  Example Response:
  ```json
  {
    "facebook_post": "Learn about Agile Methodology and improve your team's performance. #Agile #ProjectManagement",
    "video_script": "In today's video, we will explore the fundamentals of Agile Methodology and how it can help your team deliver better results."
  }
  ```

## Troubleshooting

- **CORS Issue**: If you're running the frontend locally (e.g., `file://`), you might encounter a CORS error. Make sure the backend is running and accessible at `http://localhost:8000`. You can adjust CORS settings in FastAPI if needed.
- **Spinner not disappearing**: Ensure the FastAPI server is running and reachable, as the spinner depends on the backend responding successfully.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.