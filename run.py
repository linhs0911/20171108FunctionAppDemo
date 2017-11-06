import os
import json
import pandas

postreqdata = json.loads(open(os.environ['req']).read())

data = postreqdata['currency']

dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

currency = dfs[0]

currency = currency.iloc[:,0:5]

currency.columns = [u'currency',u'CashBankBuy',u'CashBankSold',u'SpotBankBuy',u'SpotBankSold']

currency[u'currency'] = currency[u'currency'].str.extract('\((\w+)\)',expand=True)

currency = currency.iloc[currency.currency[currency.currency == data].index,0:5]

response = open(os.environ['res'], 'w')
response.write(currency.to_json())
response.close()