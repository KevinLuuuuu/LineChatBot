from transitions.extensions import GraphMachine
from utils import send_text_message, send_button_message
from linebot import LineBotApi
from linebot.models import MessageTemplateAction, FlexSendMessage, ImageSendMessage
import os

import box_message, about_rabbit_template

import requests
from bs4 import BeautifulSoup

weight = 0.0
age = 0.0
location = ""
feed_or_water_or_grass = ''
index1 = 0
index2 = 0
index3 = 0


def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = box_message.main_menu
        message_to_reply = FlexSendMessage("主選單", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_ptt(self, event):
        text = event.message.text
        if(text == "ptt"):
            return True
        else: 
            return False
    def on_enter_ptt(self, event):
        reply_token = event.reply_token
        message = box_message.show_ptt

        url="https://www.ptt.cc/bbs/rabbit/index.html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.select("div.title")
        title = []
        url = []
        for item in results:
            a_item = item.select_one("a")
            if a_item:
                title.append(item.text)
                url.append('https://www.ptt.cc'+ a_item.get('href'))
        
        sequences = [0, 1, 2, 3, 4]
        for i in sequences:
            message['contents'][i]['body']['contents'][0]['action']['uri'] = url[len(url)- 5 - i]
            message['contents'][i]['body']['contents'][0]['action']['label'] = title[len(title) - 5 - i]
        
        message_to_reply = FlexSendMessage("PTT", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
    

    def is_going_to_show_fsm(self, event):
        text = event.message.text
        if(text == "fsm"):
            return True
        else: 
            return False

    def on_enter_show_fsm(self, event):
        image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/KEBltE5.png',
        preview_image_url='https://i.imgur.com/KEBltE5.png')
        reply_token = event.reply_token
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, image_message)

        self.go_back()

    def is_going_to_water(self, event):
        text = event.message.text
        return text == "水"

    def on_enter_water(self, event):
        global feed_or_water_or_grass 
        feed_or_water_or_grass = '水'
        reply_token = event.reply_token
        message = box_message.water_menu
        message_to_reply = FlexSendMessage("關於喝水", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_input_weight(self, event):
        global age, feed_or_water_or_grass
        text = event.message.text
        if(feed_or_water_or_grass == '水' and text == "水量"):
            return True
        if(feed_or_water_or_grass == '飼料' and check_float(text)):
            age = float(text)
            if(age<0):
                return False
            return True
        return False

    def on_enter_input_weight(self, event):
        send_text_message(event.reply_token, '你家的兔兔多重呢 ? (KG)')

    def is_going_to_water_volume(self, event):
        global weight, feed_or_water_or_grass
        text = event.message.text
        if (check_float(text) and feed_or_water_or_grass == '水'):
            weight = float(text)
            if(weight<0):
                return False
            return True
        else:
            return False

    def on_enter_water_volume(self, event):
        global weight
        water_volume = round(weight*1000*0.12)
        reply_token = event.reply_token
        message = box_message.show_water
        message['body']['contents'][1]['text'] = str(water_volume) + " 毫升的水哦 !"
        message_to_reply = FlexSendMessage("所需水量", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_precautions(self, event):
        global feed_or_water_or_grass
        text = event.message.text
        if((feed_or_water_or_grass == '水' or feed_or_water_or_grass == '飼料' or feed_or_water_or_grass == '草') and text == "注意事項"):
            return True
        else:
            return False

    def on_enter_precautions(self, event):
        global feed_or_water_or_grass
        if(feed_or_water_or_grass == '水'):
            send_text_message(event.reply_token, '給兔子餵水一定要準備乾淨的容器哦，要注意每24小時一定要更換一次乾淨且煮開過的水，因為兔子的消化道很脆弱，在喝水品質一定要嚴格把關才行 \n\n輸入『主選單』可回主選單')
        elif(feed_or_water_or_grass == '飼料'):
            send_text_message(event.reply_token, '飼料一定要新鮮，盡量可以選擇纖維質含量高的。不過要注意雖然飼料能提供許多營養給兔兔，但飼料其實並非兔子的主食呦，兔奴們必須以牧草為主，飼料為輔，對兔兔的健康才是最好的 \n\n輸入『主選單』可回主選單')
        elif(feed_or_water_or_grass == '草'):
            send_text_message(event.reply_token, '要注意乾草才是對兔子們來說最重要的食物，吃草可以幫助他們磨牙 + 促進腸胃蠕動排便順暢，因此如果家裡兔兔不吃草的話很容易就會生病的，一定要小心 \n\n輸入『主選單』可回主選單')
        self.go_back()

    def is_going_to_feed(self, event):
        text = event.message.text
        return text == '飼料'

    def on_enter_feed(self, event):
        global feed_or_water_or_grass
        feed_or_water_or_grass = '飼料'
        reply_token = event.reply_token
        message = box_message.feed_menu
        message_to_reply = FlexSendMessage("關於飼料", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_input_age(self, event):
        text = event.message.text
        if((feed_or_water_or_grass == '飼料' and text == "飼料量") or (feed_or_water_or_grass == '草' and text == "哪種草")):
            return True
        else:
            return False
        
    def on_enter_input_age(self, event):
        send_text_message(event.reply_token, '你家的兔兔幾歲呢 ? (歲)')

    def is_going_to_feed_amount(self, event):
        global weight
        text = event.message.text
        if (check_float(text) and feed_or_water_or_grass == '飼料'):
            weight = float(text)
            if(weight<0):
                return False
            return True
        else:
            return False

    def on_enter_feed_amount(self, event):
        global weight, age
        what_feed = ''
        #3～5%
        if(age<0.8):
            what_feed = '幼兔專用飼料'
        elif(age>=0.8 and age <=6):
            what_feed = '成兔高纖飼料'
        elif(age>6):
            what_feed = '老兔專用飼料'
        amount_of_feed1 =  round(weight*1000*0.03)
        amount_of_feed2 =  round(weight*1000*0.05)
        spoon1 = round(amount_of_feed1/11)
        spoon2 = round(amount_of_feed2/11)
        reply_token = event.reply_token
        message = box_message.show_feed
        message['body']['contents'][0]['text'] = "你家的兔兔適合" + what_feed
        message['body']['contents'][2]['text'] = str(amount_of_feed1) + "~" + str(amount_of_feed2) + "公克的飼料哦 !"
        message['body']['contents'][3]['text'] = "大約是" + str(spoon1) + "~" + str(spoon2) + "匙的量"
        message_to_reply = FlexSendMessage("飼料量", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_input_location(self, event):
        text = event.message.text
        return text == "地點"
        
    def on_enter_input_location(self, event):
        send_text_message(event.reply_token, '請輸入你現在的所在位置(縣市、區等等)')

    def is_going_to_pet_shop(self, event):
        global location
        text = event.message.text
        location = text
        return True
        return False

    def on_enter_pet_shop(self, event):#try
        global location
        URL = 'https://www.google.com.tw/maps/search/' + location + '寵物店'
        send_text_message(event.reply_token, URL + " \n點選網址查詢你周圍的寵物店家 \n\n輸入『地點』可重新輸入地點 \n輸入『主選單』可回主選單")

    def is_going_to_grass(self, event):
        text = event.message.text
        return text == '草'
    
    def on_enter_grass(self, event):
        global feed_or_water_or_grass
        feed_or_water_or_grass = '草'
        reply_token = event.reply_token
        message = box_message.grass_menu
        message_to_reply = FlexSendMessage("關於草", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_grass_amount(self, event):
        global age, feed_or_water_or_grass
        text = event.message.text
        if(feed_or_water_or_grass == '草' and check_float(text)):
            age = float(text)
            if(age<0):
                return False
            return True
        return False

    def on_enter_grass_amount(self, event):
        global age
        reply_token = event.reply_token
        message = box_message.show_grass
        if(age<0.6):
            message['body']['contents'][1]['text'] = "苜蓿草和果園草哦 !"
        else:
            message['body']['contents'][1]['text'] = "提摩西草、甜燕麥牧草和"
            message['body']['contents'][2]['text'] = "果園草哦 !"
        message_to_reply = FlexSendMessage("哪種草", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_about_rabbit(self, event):
        text = event.message.text
        return text == "知識" or text == "其他"

    def on_enter_about_rabbit(self, event):
        reply_token = event.reply_token
        message = box_message.about_rabbit_menu
        message_to_reply = FlexSendMessage("兔兔の小知識", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_diet(self, event):
        text = event.message.text
        return text == "飲食"    
    
    def on_enter_diet(self, event):
        global index1
        send_text_message(event.reply_token, about_rabbit_template.diet_dict[index1]+"\n\n輸入『主選單』可回主選單\n輸入『其他』或點選選單中的項目可再看其他有關兔兔的知識喔")
        index1 = index1 + 1
        if(index1 == 11):
            index1 = 0

    def is_going_to_body_language(self, event):
        text = event.message.text
        return text == "肢體語言"
    
    def on_enter_body_language(self, event):
        global index2
        send_text_message(event.reply_token, about_rabbit_template.body_language_dict[index2]+"\n\n輸入『主選單』可回主選單\n輸入『其他』或點選選單中的項目可再看其他有關兔兔的知識喔")
        index2 = index2 + 1
        if(index2 == 12):
            index2 = 0

    def is_going_to_trivia(self, event):
        text = event.message.text
        return text == "冷知識"

    def on_enter_trivia(self, event):
        global index3
        send_text_message(event.reply_token, about_rabbit_template.trivia_dict[index3]+"\n\n輸入『主選單』可回主選單\n輸入『其他』或點選選單中的項目可再看其他有關兔兔的知識喔")
        index3 = index3 + 1
        if(index3 == 11):
            index3 = 0
