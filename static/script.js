const chatbox = document.getElementById("chatbox");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

sendButton.addEventListener("click", () => {
    const userMessage = userInput.value;
    if (userMessage) {
        displayMessage(userMessage, "user");
        userInput.value = "";
        getBotResponse(userMessage);
    }
});

function displayMessage(message, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(sender === "user" ? "user-message" : "bot-message");
    const img = document.createElement("img");
   img.src = sender === "user" ? "../static/clown.jpg" : "/static/doctor.jpg"; 
    img.classList.add("message-avatar"); 
    messageDiv.appendChild(img);
    messageDiv.appendChild(document.createTextNode(message));
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight; 
}

function getBotResponse(userMessage) {
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage }) 
    })
    .then(response => response.json()) 
    .then(data => {
        displayMessage(data.response, "bot");
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage("Sorry, there was an error with your request.", "bot");
    });
}

document.getElementById("user-input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        const userMessage = userInput.value;
    if (userMessage) {
        displayMessage(userMessage, "user");
        userInput.value = "";
        getBotResponse(userMessage);
    }
    }
});