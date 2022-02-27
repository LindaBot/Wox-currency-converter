# -*- coding: utf-8 -*-

import coinmarketcapapi
import json
import os
import re
from wox import Wox
from wox import WoxAPI

API_KEY = json.load(open("config.json"))["CMC_API_KEY"]
cmc = coinmarketcapapi.CoinMarketCapAPI(API_KEY)

convertPattern = re.compile(r'(\b\d[\d,.]*)\s?([a-zA-Z]+)\s?to\s?([a-zA-Z]+)')
convertPattern1 = re.compile(r'(\b\d[\d,.]*)\s?([a-zA-Z]+)')

def extract_sentence(string):
    match = convertPattern.match(string)
    if (match == None):
        match = convertPattern1.match(string)
        if (match == None):
            exit()
        amount, fromCoin = match.groups()
        return amount.replace(",",""), fromCoin, "USD"
    else:
        amount, fromCoin, toCoin = match.groups()
        return amount.replace(",",""), fromCoin, toCoin

def convert(fromCoin, toCoin, amount):
    fromCoin = fromCoin.upper()
    toCoin = toCoin.upper()
    tool=cmc.tools_priceconversion(amount=amount, symbol=fromCoin, convert=toCoin)
    cmcResponse = tool.data
    responseString = str(cmcResponse["amount"]) + " " + cmcResponse["symbol"] + " to " + toCoin + " is " + str(cmcResponse["quote"][toCoin]["price"])
    amount = str(cmcResponse["quote"][toCoin]["price"])
    return amount, responseString

def process_crypto_convert(string):
    amount, fromCoin, toCoin = extract_sentence(string)
    return convert(fromCoin, toCoin, amount)

def copy2clip(txt):
    command = 'echo ' + txt.strip() + '| clip'
    os.system(command)

class HelloWorld(Wox):
    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        amount, responseString = process_crypto_convert(query)
        results = []
        results.append({
            "Title": str(amount),
            "SubTitle": "{}".format(responseString),
            "IcoPath":"Images/app.png",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                'method': 'take_action',
                'parameters': ["{}".format(amount)],
                'dontHideAfterAction': False
            }
        })
        return results

    # context_menu is default function called for ContextData where `data = ctxData`
    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.png"
        })
        return results

    def take_action(self, amount):
        # Choose what to trigger on pressing enter on the result.
        # use SomeArgument to do something with data sent by parameters.
        # WoxAPI.("title", "sub_title")
        # WoxAPI.change_query(amount)
        copy2clip(str(amount))
        return None

if __name__ == "__main__":
    HelloWorld()

def test():
    amount, responseString = process_crypto_convert("500USD to NZD")
    print(amount, responseString)
