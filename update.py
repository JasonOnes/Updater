from googlefinance import getQuotes
import json
import requests
from moneyed import Money, USD
from twilio.rest import Client 



def getQuote(fundname):
    """retrieves the last price for fund"""
    try:
        info = json.dumps(getQuotes(fundname))
        data = json.loads(info)
        data_dict = {k: v for d in data for k, v in d.items()}
        return(data_dict['LastTradePrice'])
    except URLError:
        msg = """Cannot connect to URL right now, check web connection or try
        later."""
        return msg

def current_value(fundname, num_shares):
    quote = getQuote(fundname)
    price = Money(quote, currency='USD')
    value = num_shares * price
    msg = "Today you hold " + str(value) + " of {}.".format(fundname)
    return msg

def send_quote(fundname, num_shares, phone_num):# ,time_of_day)
    msg = current_value(fundname, num_shares)
    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=str(phone_num),
        from_="xxxxxxxxxx",
        body=msg
    )
    return print(message.sid)

if __name__ == "__main__":
    
    send_quote('VGPMX', 381.679, #)