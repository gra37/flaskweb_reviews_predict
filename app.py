from classifier import Classifier
from codecs import open
import json
import time
from flask import Flask, render_template, request
import random
import pandas as pd

app = Flask(__name__)



print("Load classifier")
start_time = time.time()
classifier = Classifier()
print("Classifier is successfully loaded")
print(time.time() - start_time, "seconds")


df = pd.read_csv('df_kinopoisk_shuffle.csv')
df.columns = ['unnamed', 'rev', 'mood', 'text_edited',
       'text_edited_2', 'labels']

@app.route("/", methods = ["POST", "GET"])
def index_page(text = "", prediction_message = ""):

    if request.method == "POST":
        text = request.form["text"]

        # logfile = open("rews_demo_logs.txt", "ab", "utf-8")
        #
        # # print(text)
        # logfile.write(text)
        # logfile.write("<response>")

        prediction_message = classifier.get_result_message(text)

        # # print(prediction_message)
        # logfile.write(prediction_message)
        # logfile.write("<response>")
        #
        # logfile.close()

    reviews = df.sample(n=15, random_state=1).to_dict(orient = 'index')
    return render_template('index.html', text = text, prediction_message = prediction_message, reviews = reviews)


if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 4000, debug = True)
