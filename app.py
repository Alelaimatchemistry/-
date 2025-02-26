
from flask import Flask, request, jsonify

app = Flask(__name__)

# Chatbot logic function
def chatbot_query(user_input):
    user_input = user_input.lower()
    if "concept" in user_input:
        response = "Here are some concepts:\n- Concept 1: Description\n- Concept 2: Description"
    elif "tool" in user_input or "project" in user_input:
        response = "Here are some tools/projects:\n- Tool 1: Description\n- Tool 2: Description"
    elif "idea" in user_input:
        response = "Here are some innovative ideas:\n- Idea 1: Description\n- Idea 2: Description"
    elif "attribute" in user_input:
        response = "Here are some attributes:\n- Attribute 1: Description\n- Attribute 2: Description"
    else:
        response = "Sorry, I didn't understand your request. Try asking about concepts, tools, ideas, or attributes."
    return response

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = chatbot_query(user_input)
    return jsonify({"response": response})

@app.route("/", methods=["GET"])
def home():
    return '''
    <html>
    <head>
        <title>AI Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; }
            #chatbox { width: 100%; height: 300px; border: 1px solid #ccc; padding: 10px; overflow-y: auto; }
            #message { width: 80%; }
            button { padding: 5px 10px; }
        </style>
    </head>
    <body>
        <h1>Welcome to the AI Chatbot</h1>
        <div id="chatbox"></div>
        <input type="text" id="message" placeholder="Type your message here">
        <button onclick="sendMessage()">Send</button>
        <script>
            function sendMessage() {
                let message = document.getElementById('message').value;
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                })
                .then(response => response.json())
                .then(data => {
                    let chatbox = document.getElementById('chatbox');
                    chatbox.innerHTML += "<p><b>You:</b> " + message + "</p>";
                    chatbox.innerHTML += "<p><b>Bot:</b> " + data.response + "</p>";
                    document.getElementById('message').value = '';
                    chatbox.scrollTop = chatbox.scrollHeight;
                });
            }
        </script>
    </body>
    </html>
    '''

# Run the application (for local testing)
if __name__ == "__main__":
    app.run(debug=True)
