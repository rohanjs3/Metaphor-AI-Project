from flask import Flask, jsonify, request
from stock_news import fetch_stock_news
from summarizer import fetch_and_aggregate_articles
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stock_tickers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_stocks', methods=['POST'])
def add_stocks():
    global stock_tickers
    tickers = request.json.get('tickers', [])
    stock_tickers.extend(tickers)  # Add the provided tickers to the global list
    stock_tickers = list(set(stock_tickers))  # Remove duplicates
    return jsonify({"message": "Stocks added successfully!"})


@app.route('/get_news')
def get_news():
    news = fetch_stock_news(stock_tickers)  # Pass the global stock_tickers list
    summarized_news = {ticker: fetch_and_aggregate_articles(article) for ticker, article in news.items()}
    return jsonify(str(summarized_news))



if __name__ == '__main__':
    app.run(debug=True)
