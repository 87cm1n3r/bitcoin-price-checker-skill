from mycroft import MycroftSkill, intent_file_handler


class BitcoinPriceChecker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('checker.price.bitcoin.intent')
    def handle_checker_price_bitcoin(self, message):
        self.speak_dialog('checker.price.bitcoin')


def create_skill():
    return BitcoinPriceChecker()

