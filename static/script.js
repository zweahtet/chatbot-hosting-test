const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// Icons made by Freepik from www.flaticon.com
const BOT_IMG = "./icons/dialogflow-insights-svgrepo-com.svg";
const PERSON_IMG = "";
const BOT_NAME = "    ChatBot";
const PERSON_NAME = "You";

msgerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";
    botResponse(msgText);
});

function appendMessage(name, img, side, text) {
    //   Simple solution for small apps
    const msgHTML = `
                <div class="msg ${side}-msg">
                <div class="msg-img" style="background-image: url(${img})"></div>

                <div class="msg-bubble">
                    <div class="msg-info">
                        <div class="msg-info-name">${name}</div>
                        <div class="msg-info-time">${formatDate(
                            new Date()
                        )}</div>
                    </div>

                    <div class="msg-text">${text}</div>
                </div>
                </div>
            `;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

async function botResponse(text) {
    // Bot Response
    const response = await fetch("chat?input=${text}");
    const json = await response.json();

    console.log(text);
    console.log(json);

    appendMessage(BOT_NAME, BOT_IMG, "left", json.bot_reply);
}

// Utils
function get(selector, root = document) {
    return root.querySelector(selector);
}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}
