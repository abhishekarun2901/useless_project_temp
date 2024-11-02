import flask
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open("chatbot.pkl", 'rb') as f:
    chat = pickle.load(f)


fallback_response = "I really want to help you...But I won't...Is there anything else I can help you with??"

@app.route("/chat") 
def chatbot():
    return render_template("chat.html")  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data["message"]

    if user_input.lower() == 'quit':
        return jsonify({"response": "Goodbye! I was just starting to figure this therapist thing out."})
    
    response = chat.respond(user_input)
    if response is None:
        response = fallback_response

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
