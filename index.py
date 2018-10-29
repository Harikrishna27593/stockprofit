from flask import Flask
from flask import render_template
from flask import request
from requests.exceptions import ConnectionError
import requests
import json

app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"


@app.route("/ajax", methods=['POST','GET'])
def listener():


	tickerSymbol = request.form['tickerSymbol'];
	Allotment = int(request.form['Allotment']);
	Final_share_price = int(request.form['Final_share_price']);
	Sell_commission = int(request.form['Sell_commission']);
	Initial_share_price = int(request.form['Initial_share_price']);
	Buy_commission = int(request.form['Buy_commission']);
	Captial_gain_tax_rate = int(request.form['Captial_gain_tax_rate']);

	print tickerSymbol

	print "\n your report is generated"

	proceeds = Allotment*Final_share_price


	cost = (Allotment*Initial_share_price)+Buy_commission+Sell_commission+(Captial_gain_tax_rate*0.01)

	Totalprice = Allotment*Initial_share_price



	Taxoncapitalgain = (proceeds-(Initial_share_price*Allotment)-Buy_commission-Sell_commission)*Captial_gain_tax_rate*0.01

	netprofit = proceeds-cost-Taxoncapitalgain

	s=  netprofit/cost
	n= s*100


	breakeven= Initial_share_price+Initial_share_price*0.01


	data = {
	'tickerSymbol': tickerSymbol,
    'Allotment': Allotment,
    'Final_share_price': Final_share_price,
	'Initial_share_price': Initial_share_price,
    'Captial_gain_tax_rate': Captial_gain_tax_rate,
    'proceeds': proceeds,
    'cost': cost,
	'Totalprice': Totalprice,
    'Buy_commission': Buy_commission,
	'Sell_commission': Sell_commission,
    'Taxoncapitalgain': Taxoncapitalgain,
	'netprofit': netprofit,
    'Return_on_Investment': n,
	'breakeven': breakeven,
	'total':(proceeds-cost)*Captial_gain_tax_rate

}


	return render_template('result.html',data=data);


@app.route("/", methods=['POST', 'GET'])
def index():

	return render_template('form.html')


app.debug = True
app.run()
