# Sentiment-Analysis-using-IBM-Watson-AI
# 🧠 NLP Sentiment Analysis using BERT (Flask + Transformers)

This is a simple yet powerful web-based **Sentiment Analysis** application built using **Flask** (Python backend) and the **Hugging Face Transformers** library. It allows users to input custom text and get real-time sentiment predictions (positive or negative) using the `distilbert-base-uncased-finetuned-sst-2-english` BERT model.

## 📸 Screenshot
<img width="1919" height="874" alt="Screenshot 2025-07-16 230707" src="https://github.com/user-attachments/assets/5656e1f4-606b-46ef-acf9-0ec9ccb6c696" />



## 🧰 Tech Stack

| Component         | Technology                                      |
|-------------------|-------------------------------------------------|
| 🧠 NLP Model      | Hugging Face `transformers` (DistilBERT SST-2) |
| 🖥 Backend        | Flask (Python 3.12)                             |
| 🖼 Frontend       | HTML, Bootstrap 4                               |
| 🔁 AJAX          | JavaScript + Fetch/XMLHttpRequest               |

---

## 🚀 Features

- ✅ Real-time sentiment analysis
- ✅ Uses pretrained BERT model (`distilbert-base-uncased-finetuned-sst-2-english`)
- ✅ Responsive UI with Bootstrap
- ✅ AJAX-based request handling (no page reload)
- ✅ Error handling and confidence score display

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-bert-flask.git
cd sentiment-analysis-bert-flask
````

### 2. Create a virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # On Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, use:

```bash
pip install flask transformers torch
```

### 4. Run the Flask app

```bash
python server.py
```

## 📁 Project Structure

```
.
├── server.py
├── SentimentAnalysis/
│   └── sentiment_analysis.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── test_sentiment_analysis.py
└── README.md
```

## 🧪 Sample Output

Input:

> This product is amazing!

Output:

```
Label: POSITIVE
Confidence Score: 0.998
```


## 🚧 Future Enhancements

* [ ] Add support for multilingual sentiment models (e.g., `nlptown/bert-base-multilingual`)
* [ ] Deploy to a live web server (Render, Heroku, or PythonAnywhere)
* [ ] Add sentiment highlighting (color-based feedback)
* [ ] Improve error and edge-case handling
* [ ] Add feedback and reset button


## 🧪 Testing

Basic unit test is available using Python's `unittest` module:

```bash
python test_sentiment_analysis.py
```
Achieved a pylint score of 10.0/10.0

## 📄 License

This project is open-source and available under the MIT License.


## 🙌 Acknowledgements

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [Flask Framework](https://flask.palletsprojects.com/)
* [Bootstrap](https://getbootstrap.com/)



