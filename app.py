# coding:utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('okOGYzp+iyx6nTHJHQF7Ts/p3PEWeYAjCvtWJoyKqyGvKXTuFEO3YBsRJDbxBhyOkiqLel6cvkl0Mavvh9NqAaXcaXp2TFrOvQSXn8Sm+iz2/NbGqrrS7f09epSkG7/q6RBgXtSwrNw8RbNdfD6Q8gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a8ed97ba16dfc92b59e3970b8061b5a7')
def random():
    
    number=random.randint(0,6)
    return number
def txt(s):
    b=[]
    d=[]
    file=open('data/'+s+'.txt', encoding = 'utf-8')        
    for line in file:
        b.append(line)
    file.close()
    for i in range(0,len(b)):
        c=[]
        c=b[i].split('\n')
        d.append(c[0])
    return d


def find(s,str):
    b=[]
    d=[]
    file=open('data/'+s+'.txt', encoding = 'utf-8')        
    for line in file:
        b.append(line)
    file.close()
    for i in range(0,len(b)):
        if b[i].find(str)>=0:
            c=[]
            c=b[i].split('\n')
            d.append(c[0])
    return d

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

picture=['https://www.dropbox.com/s/ntthhnhaibd5elw/1.jpg?dl=1','https://www.dropbox.com/s/48k3tf6fghvvmmo/2.jpg?dl=1','https://www.dropbox.com/s/xloc906sorulbg9/3.jpg?dl=1']
picture.append('https://www.dropbox.com/s/gm2qvbvsi6sy7ow/4.jpg?dl=1')
picture.append('https://www.dropbox.com/s/ke7zd8l02gsvya6/5.jpg?dl=1')
picture.append('https://www.dropbox.com/s/tq731xhk7vknqum/6.jpg?dl=1')
picture.append('https://www.dropbox.com/s/1euxfftx7gj94pg/7.jpg?dl=1')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    import random
    if event.message.text=='小詹照片':
        w=random.randint(0,6)
        image_message = ImageSendMessage(original_content_url=picture[w],preview_image_url=picture[w])       
        line_bot_api.reply_message(event.reply_token,image_message)
    elif event.message.text=='功能':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='可用指令:\n搜尋 關鍵字\n語錄'))
    elif event.message.text.find("語錄")>=0:
        if len(txt('else'))!=0:
            number=random.randint(0,len(txt('else'))-1)
            b=txt('else')
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=b[number]))
    elif event.message.text.find("搜尋")>=0:
        q=[]
        q=event.message.text.split(' ')
        if len(q)>1:
            if len(find('else',q[1]))!=0:
                if len(find('else',q[1]))==1:
                    number=0
                else:
                    number=random.randint(0,len(find('else',q[1]))-1)
                
                b=find('else',q[1])
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=b[number]))
    elif event.message.text.find("by")>=0:
        if event.message.text.find("搜尋")<0:
            file=open('data/else.txt','a', encoding = 'utf-8')
            file.write(event.message.text+"\n")
            file.close()
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="已儲存"))    
if __name__ == "__main__":
    app.run()
    

    
    
    
    