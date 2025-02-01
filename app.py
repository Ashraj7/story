from flask import Flask, render_template, request, session
import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

app = Flask(__name__)
app.secret_key = os.urandom(24)

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("GEMINI_API_KEY environment variable not set. Check your .env file.")

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="You are a creative and imaginative storyteller. You excel at crafting compelling narratives with vivid descriptions and engaging dialogue. You *must* provide the user with 3 numbered choices (1., 2., 3.) at the end of each part of the story.",
)

@app.route("/", methods=["GET", "POST"])
def adventure():
    if "history" not in session:
        session["history"] = []
        session["story_started"] = False
        session["choices"] = []
        session['story_state'] = 'start'

    gemini_history = []
    for item in session["history"]:
        gemini_history.append({"role": item["role"], "parts": [{"text": item["content"]}]})

    chat_session = model.start_chat(history=gemini_history)

    if request.method == "POST":
        if not session["story_started"]:
            character_name = request.form.get("character_name")
            character_trait = request.form.get("character_trait")

            if character_name and character_trait:
                initial_prompt = f"Our story begins with {character_name}, a {character_trait} traveler, embarking on a journey through the hills. {character_name} sets off... (rest of your initial prompt)"
                try:
                    response = chat_session.send_message(initial_prompt)
                    session["story_started"] = True
                    session["current_response"] = response.text
                    session["history"].append({"role": "user", "content": initial_prompt})
                    session["history"].append({"role": "model", "content": response.text})
                    extract_choices(response.text, session)
                    session['story_state'] = 'forest'
                    return render_template("adventure.html", background_image=get_background_image(session['story_state']), story=response.text, choices=session["choices"])
                except Exception as e:
                    return render_template("adventure.html", error=f"Error: {e}")
            else:
                return render_template("adventure.html", error="Please enter character name and trait.")

        else:
            user_choice = request.form.get("choice")
            if user_choice:
                try:
                    user_choice = int(user_choice)
                    if 1 <= user_choice <= len(session["choices"]):
                        response = chat_session.send_message(str(user_choice))
                        session["current_response"] = response.text
                        session["history"].append({"role": "user", "content": str(user_choice)})
                        session["history"].append({"role": "model", "content": response.text})
                        extract_choices(response.text, session)

                        if user_choice == 1:
                            session['story_state'] = 'cave'
                        elif user_choice == 2:
                            session['story_state'] = 'mountain'
                        return render_template("adventure.html", background_image=get_background_image(session['story_state']), story=response.text, choices=session["choices"])
                    else:
                        return render_template("adventure.html", story=session["current_response"], choices=session["choices"], error=f"Invalid choice. Please enter a number between 1 and {len(session['choices'])}.")
                except (ValueError, Exception) as e:
                    return render_template("adventure.html", error=f"Error: {e}")
            elif request.form.get("end") == "End Story":
                session.clear()
                return render_template("adventure.html", message="Story Ended.")
            else:
                return render_template("adventure.html", story=session["current_response"], choices=session["choices"], error="Please select a choice.")

    return render_template("adventure.html", background_image=get_background_image(session.get('story_state', 'start')))

def extract_choices(text, session):
    import re
    choices = re.findall(r"\d+\.\s*(.+?)(?=\d+\.|$)", text, re.DOTALL)
    session["choices"] = [choice.strip() for choice in choices]

def get_background_image(story_state):
    if story_state == "forest":
        return "forest.jpg"
    elif story_state == "cave":
        return "cave.png"
    elif story_state == "mountain":
        return "mountain.gif"
    elif story_state == "start":
        return "start.jpg"
    else:
        return "default.jpg"

if __name__ == "__main__":
    app.run(debug=True)