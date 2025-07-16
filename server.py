''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get("textToAnalyze", "")
    if not text:
        return "Please provide text for sentiment analysis."
    result = sentiment_analyzer(text)
    label= result.get("label", "Error")
    score = result.get("score", "N/A")
    return f"Sentiment: {label}, Confidence Score: {score}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
