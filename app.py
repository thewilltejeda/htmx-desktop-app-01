from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stocks")
def send_updated_stocks():
    tickers = [
        "AAPL",
        "GOOGL",
        "RIVN",
        "TSLA",
        "MSFT",
       
    ]

    innerHTML = ""

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hourly_data = stock.history(period="5d", interval="1d")

        latest_price = hourly_data["Close"].iloc[-1]
        previous_price = hourly_data["Close"].iloc[-2]

        percentage_change = ((latest_price - previous_price) / previous_price) * 100

        innerHTML += f"""
            <div class="p-2 items-center w-48 stock p-4 text-black/90 justify-center shadow-lg border-2 border-black/20 bg-gradient-to-b from-white/70 to-yellow-300 rounded-2xl">
                <p  class="font-semibold text-3xl text-center font-serif">{ticker}</p>
                <a href="https://www.tradingview.com/chart/?symbol={ticker.upper()}" target="_blank" >
                    <div class="flex items-center justify-center drop-shadow-md bg-white/80 rounded-xl p-2 mt-1 shadow-lg {"text-green-500" if percentage_change > 0 else "text-red-500"}">
                        <p class="text-center text-sm font-semibold mx-auto">
                            {"↑" if percentage_change > 0 else "↓"}
                        </p>
                        
                        <p class="text-center text-sm font-semibold mx-auto  -ml-1">
                            {percentage_change:.2f}%
                        </p>
                        <p class="text-xl text-center text-black pr-1 font-serif">${latest_price:.2f}</p>

                    </div>
                </a>
            </div>
         """

        result = f"""
            <div class="flex flex-wrap gap-4 items-center justify-center">
                {innerHTML}
            </div>
        """

    return result

if __name__ == "__main__":
    app.run(debug=True)