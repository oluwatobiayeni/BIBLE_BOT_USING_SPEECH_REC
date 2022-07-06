from flask import Flask, render_template, request
import random
from bible_study import manual
from scripture_search import auto
import speech_recognition as sr
import asyncio


loop = asyncio.get_event_loop()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    text = ""
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def result():
    # GlobalRe Run_Troy()'
    globalConversation = []
    quotes = manual()
    # quotes = [
    #     "Instagram is not the answer.",
    #     "You can discover everything you need to know about everything by looking at your hands",
    #     "Being born was the most influential thing that’s ever happened to me, for myself.",
    #     "When Life Gives You Big Problems, Just Be Happy You Forgot All Your Little Problems.",
    #     "The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy.",
    #     "When The First Animal Went Extinct That Should've Been A Sign.",
    #     "How Can Mirrors Be Real If Our Eyes Aren't Real."
    # ]
    # quote = "%s -- Jaden Smith" % random.choice(quotes)
    return render_template('result.html', randomQuote=quotes)


@app.route("/test", methods=['GET', 'POST'])
def test():
    conversation=auto()
    return render_template('test.html',cvHistory=conversation)



    # Run_Troy()
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


# import asyncio


# async def async_get_data():
#     await asyncio.sleep(1)
#     return 'Done!'

# @app.route('/galleries')
# def galleries():
#     if 'type' in session:
#         gallery_obj = Gallery()
#         galleries = gallery_obj.get_all_gallery()
#         return render_template("gallery.html", galleries=galleries, session=session)
#     else:
#         return redirect(url_for("index"))


# @app.route('/galleries/add', methods=['POST'])
# def add_galleries():
#     if 'type' in session:
#         if request.method == "POST":
#             gallery_name = request.form['galleryName']

#             gallery_obj = Gallery()
#             result = gallery_obj.add_gallery(gallery_name)

#             response = {'success':result}
#             return json.dumps(response)
#     else:
#         response = {'success': False}
#         return json.dumps(response)



if __name__ == "__main__":
    print('Running')
    app.run()
    #print('Running')