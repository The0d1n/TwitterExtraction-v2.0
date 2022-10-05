_author_ = 'chan'

import twint
from textwrap import indent
from flask import Flask, make_response, render_template, request, jsonify, json
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html_page.html')

@app.route('/result', methods=['POST'])
def result():
    keyword = request.form['keyword']
    location = request.form['location']
    config = twint.Config()
    config.Search = keyword
    config.Near = location
    config.Pandas = True
    config.Limit = 30
    config.Store_csv = True
    config.Output = "tweets.csv"
    
    twint.run.Search(config)
    twint.storage.panda.Tweets_df.to_csv("tweets.csv")

    df = pd.read_csv('tweets.csv')
    df.to_csv('tweets.csv', index=None)
    data = pd.read_csv('tweets.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)