from mycroft import MycroftSkill, intent_file_handler
import requests
import json

class BitcoinPriceChecker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('checker.price.bitcoin.intent')
    def handle_checker_price_bitcoin(self, message):
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        j = json.loads(r.content)
        d, c = str(j['bpi']['USD']['rate_float']).split('.')

        self.speak_dialog(d + ' dollars and ' + c + ' cents')


def create_skill():
    return BitcoinPriceChecker()

