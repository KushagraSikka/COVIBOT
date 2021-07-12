from chat1 import chatbot_response
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/get")
def get_bot_response():
    UserTxt=request.args.get('msg')
    resp=chatbot_response(UserTxt)
    return str(resp)
   

if __name__ == "__main__":
    app.run()
