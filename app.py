from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple function to simulate an AI response
def get_ai_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you with Aura today?",
        "features": "Aura offers chat, streaming, and music features. You can stream, chat with friends, and enjoy high-quality music.",
        "download": "You can download Aura on Windows, Mac, iOS, and Android.",
        "premium": "Aura Premium offers 4K streaming, offline music, and much more."
    }
    # Return a response based on user input, defaulting to a generic response
    return responses.get(user_input.lower(), "Sorry, I didn't quite get that. Can you ask about Aura features?")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    ai_response = get_ai_response(user_input)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
  
