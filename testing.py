import os

class Twilio(object):

    auth_token = '32d05e690e3c1ecb0d925d27f671e881'
    twilio_command = ''

    def __init__(self):
        pass

    def sms_price(self, recipient_phone_number, price):
        twilio_command = """
        curl -X POST 'https://api.twilio.com/2010-04-01/Accounts/ACe890e4859ded6e20abcd7a0c630a8aea/SMS/Messages.xml' \
        -d 'From=%2B16462487656' \
        -d 'To=""" + recipient_phone_number + """' \
        -d 'Body=XBT+Price+Alert%3A+Bitstamp+%24""" + price + """' \
        -u ACe890e4859ded6e20abcd7a0c630a8aea:""" + self.auth_token
        os.system(twilio_command)

t = Twilio()
t.sms_price('7327577624', '715.16')