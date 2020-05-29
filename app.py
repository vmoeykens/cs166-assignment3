from flask import Flask, render_template
import traceback

app = Flask(__name__)


@app.route('/')
def cat_coin_stock():
    my_netid = "jreddy1"  # Replace with your UVM NetID here!
    return render_template("CatCoin_Stock.html", netid=my_netid)


if __name__ == '__main__':
    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()
