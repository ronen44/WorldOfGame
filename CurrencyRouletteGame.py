# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random
import requests, json
from GuessGame import generate_number

from GuessGame import get_guess_from_user

def get_money_interval(total_value_of_money,difficulty):
    t = total_value_of_money
    d = 6 - difficulty
    toRet0 = t + d
    toRet1 = t - d
    return toRet0 , toRet1


def play_currency(difficulty):
    # currency code 
    from_currency = "USD"
    to_currency = "ILS"
    # enter your api key here  
    api_key = "3JKXC3A97NMG380H"
    status = False
    
    # function calling 
    #currentCurrencyExchangeRate = RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)
    currentCurrencyExchangeRate = 3.5
    number_messge = "amount in USD :"
    generate_number_amount_in_USD = generate_number(number_messge, 101)
    amount_in_ILS = currentCurrencyExchangeRate * generate_number_amount_in_USD
    guess_amount_of_money = get_guess_from_user("Please chose total value of money in ILS: ")
    get_money_interval_amount0 , get_money_interval_amount1 =  get_money_interval(amount_in_ILS,difficulty)
    print(get_money_interval_amount0)
    print(get_money_interval_amount1)
    if guess_amount_of_money <=  get_money_interval_amount0 and guess_amount_of_money >=  get_money_interval_amount1:
        print("you win")
        status = True
    else:
        print("you lost")
    return status

def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) : 
    # importing required libraries 
  
    # base_url variable store base url  
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    # main_url variable store complete url 
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
  
    # get method of requests module  
    # return response object  
    req_ob = requests.get(main_url) 
  
    # json method return json format 
    # data into python dictionary data type. 
      
    # result contains list of nested dictionaries 
    result = req_ob.json() 
  
  
    currencyExchangeRate = result["Realtime Currency Exchange Rate"] ['5. Exchange Rate']
    return currencyExchangeRate