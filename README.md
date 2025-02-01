# The Weaver's Odyssey: An Interactive Story

**Short Description:** A dynamic interactive fiction game where player choices shape the narrative, enhanced by AI-generated content and immersive background visuals.

## Problem Statement

Traditional interactive fiction often relies on pre-written content, limiting replayability and creating a static experience. Furthermore, crafting compelling narratives with branching storylines is a time-consuming process. We sought to address these limitations by leveraging the power of AI to generate dynamic and personalized stories.

## Solution Overview

The Weaver's Odyssey uses the Gemini API to generate story content in real-time, based on the player's choices. This allows for a unique and unpredictable narrative experience with each playthrough. The game also incorporates dynamic background images that change to reflect the current scene, further immersing the player in the story. Players begin by defining their character's name and a key trait, adding a personal touch to the adventure.

## Tech Stack Used

*   **Backend:** Flask (Python)
*   **Story Generation:** Gemini API
*   **Frontend:** HTML, CSS
*   **Version Control:** Git

## Setup and Installation Instructions

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/yourusername/your-repository-name.git](https://github.com/yourusername/your-repository-name.git)
    ```

2.  **Navigate to the Project Directory:**

    ```bash
    cd your-repository-name
    ```

3.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv  # Or python -m venv venv, depending on your setup
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt  # Create requirements.txt first (see below)
    ```

    *(Create `requirements.txt` by running `pip freeze > requirements.txt` after installing Flask and the Gemini API library.)*

5.  **Set Environment Variables:**

    *   Create a `.env` file in the project's root directory.
    *   Add your Gemini API key to the `.env` file:

    ```
    GEMINI_API_KEY=your_actual_api_key
    ```

    ***Important: Never commit your `.env` file to GitHub!***

6.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

7.  Open your web browser and go to the URL provided by Flask (usually `http://127.0.0.1:5000/`).

8.  video link:https://drive.google.com/drive/folders/1SExiAEPu6S-0AIy242DUx9qtAweMT2h4?usp=drive_link

## Team Contributions

*   **[Ashitha Raj B S]:** Developed the core Flask application, including routing and session management. Integrated the Gemini API for dynamic story generation. Designed and implemented the dynamic background image feature. Created the HTML templates and CSS styling.


*   "Developed the core Flask application, including routing and session management. This involved setting up the Flask app, defining the routes for handling user input and displaying the story, and implementing the session logic to maintain the player's progress and story state."
*   "Integrated the Gemini API for dynamic story generation. This involved making API calls to Gemini, processing the responses, and extracting the choices for the player."
*   "Designed and implemented the dynamic background image feature. This involved using Jinja2 templating to dynamically generate the image URLs in the HTML based on the current story state stored in Flask sessions."
*   "Created the HTML templates and CSS styling. This involved designing the layout of the game interface and creating the CSS rules to style the text, buttons, and other elements."
