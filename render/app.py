from flask import Flask, request, jsonify
import yfinance as yf
import os

app = Flask(__name__)

@app.route('/get-price', methods=['GET'])
def get_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Missing symbol parameter"}), 400
    
    try:
        ticker = yf.Ticker(f"{symbol.upper()}.NS")
        price = ticker.fast_info['last_price']
        return jsonify({
            "symbol": symbol.upper(),
            "price": round(price, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Render provides a PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
