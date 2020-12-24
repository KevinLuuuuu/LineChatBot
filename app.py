import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message

load_dotenv()


machine = TocMachine(
    states=[
    "user", "menu",
    "show_fsm", 
    "water", "input_weight", "water_volume", "precautions",  
    "feed", "input_location", "pet_shop", "input_age", "feed_amount",
    "grass", "grass_amount", 
    "about_rabbit", "diet", "body_language", "trivia",
    "ptt"],

    transitions=[

    {'trigger': 'advance', 'source': 'user', 'dest': 'menu', 'conditions': 'is_going_to_menu'},

    {'trigger': 'advance', 'source': 'menu', 'dest': 'ptt', 'conditions': 'is_going_to_ptt'},

    {'trigger': 'advance', 'source': 'menu', 'dest': 'show_fsm', 'conditions': 'is_going_to_show_fsm'},

    {'trigger': 'advance', 'source': 'menu', 'dest': 'water', 'conditions': 'is_going_to_water'},
    {'trigger': 'advance', 'source': 'water', 'dest': 'input_weight', 'conditions': 'is_going_to_input_weight'},
    {'trigger': 'advance', 'source': 'input_weight', 'dest': 'water_volume', 'conditions': 'is_going_to_water_volume'},
    {'trigger': 'advance', 'source': 'water', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},
    {'trigger': 'advance', 'source': 'water_volume', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},

    {'trigger': 'advance', 'source': 'menu', 'dest': 'feed', 'conditions': 'is_going_to_feed'},
    {'trigger': 'advance', 'source': 'feed', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},
    {'trigger': 'advance', 'source': 'feed', 'dest': 'input_age', 'conditions': 'is_going_to_input_age'},
    {'trigger': 'advance', 'source': 'input_age', 'dest': 'input_weight', 'conditions': 'is_going_to_input_weight'},
    {'trigger': 'advance', 'source': 'input_weight', 'dest': 'feed_amount', 'conditions': 'is_going_to_feed_amount'},
    {'trigger': 'advance', 'source': 'feed_amount', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},

    {'trigger': 'advance', 'source': 'feed', 'dest': 'input_location', 'conditions': 'is_going_to_input_location'},
    {'trigger': 'advance', 'source': 'input_location', 'dest': 'pet_shop', 'conditions': 'is_going_to_pet_shop'},
    {'trigger': 'advance', 'source': 'pet_shop', 'dest': 'input_location', 'conditions': 'is_going_to_input_location'},  

    {'trigger': 'advance', 'source': 'menu', 'dest': 'grass', 'conditions': 'is_going_to_grass'},
    {'trigger': 'advance', 'source': 'grass', 'dest': 'input_age', 'conditions': 'is_going_to_input_age'},
    {'trigger': 'advance', 'source': 'input_age', 'dest': 'grass_amount', 'conditions': 'is_going_to_grass_amount'},

    {'trigger': 'advance', 'source': 'grass', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},
    {'trigger': 'advance', 'source': 'grass_amount', 'dest': 'precautions', 'conditions': 'is_going_to_precautions'},

    {'trigger': 'advance', 'source': 'menu', 'dest': 'about_rabbit', 'conditions': 'is_going_to_about_rabbit'},
    {'trigger': 'advance', 'source': 'about_rabbit', 'dest': 'diet', 'conditions': 'is_going_to_diet'},
    {'trigger': 'advance', 'source': 'diet', 'dest': 'about_rabbit', 'conditions': 'is_going_to_about_rabbit'},
    {'trigger': 'advance', 'source': 'about_rabbit', 'dest': 'body_language', 'conditions': 'is_going_to_body_language'},
    {'trigger': 'advance', 'source': 'body_language', 'dest': 'about_rabbit', 'conditions': 'is_going_to_about_rabbit'},
    {'trigger': 'advance', 'source': 'about_rabbit', 'dest': 'trivia', 'conditions': 'is_going_to_trivia'},
    {'trigger': 'advance', 'source': 'trivia', 'dest': 'about_rabbit', 'conditions': 'is_going_to_about_rabbit'},

    {'trigger': 'advance', 'source': 'diet', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'body_language', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'trivia', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'water_volume', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'feed_amount', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'grass_amount', 'dest': 'menu', 'conditions': 'is_going_to_menu'},

    {'trigger': 'advance', 'source': 'show_fsm', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'water', 'dest': 'menu', 'conditions': 'is_going_to_menu'}, 
    {'trigger': 'advance', 'source': 'feed', 'dest': 'menu', 'conditions': 'is_going_to_menu'}, 
    {'trigger': 'advance', 'source': 'grass', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
    {'trigger': 'advance', 'source': 'pet_shop', 'dest': 'menu', 'conditions': 'is_going_to_menu'}, 

    {"trigger": "go_back", "source": [
    "menu",
    "show_fsm",
    "precautions",  
    "ptt"], "dest": "user"},
        #{"trigger": "go_back", "source": [
        #"menu",
        #"show_fsm",
        #"water", "input_weight", "water_volume", "precautions",  
        #"feed", "input_location", "pet_shop", "input_age", "feed_amount",
        #"grass", "grass_amount", 
        #"about_rabbit", "diet", "body_language", "trivia",
        #"ptt"], "dest": "user"},

    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請依照上面的指示或按鈕輸入哦 ~")

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "請依照上面的指示或按鈕輸入哦 ~")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    #show_fsm()
    #machine.get_graph().draw("fsm.png", prog="dot", format="png")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

