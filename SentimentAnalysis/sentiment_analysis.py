from transformers import pipeline


sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def sentiment_analyzer(text_to_analyse):
    """
    Performs sentiment analysis on the input text using a local Transformers model.
    Returns the sentiment label and confidence score.
    """

    try:
        result = sentiment_pipeline(text_to_analyse)[0]
        print(f"Sentiment Analysis Result: {result}")
        label = result["label"]
        score = round(result["score"], 3)
        if label == "5 stars" or label == "4 stars":
            label = "POSITIVE"
        elif label == "1 star" or label == "2 stars":
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        return {
            "label": label,
            "score": score
        }

    except Exception as e:
        return {
            "error": f"An error occurred during analysis: {str(e)}"
        }
    