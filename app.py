from datetime import datetime
import numpy as np
import tulipy as ti
import requests
import ccxt
from telebot import types
from telebot import util
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import telebot
import pandas as pd
import matplotlib.pyplot as plt
import talib
import json
import numpy
import schedule
from time import sleep

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Halo')
    
bot.polling(none_stop=True, interval=2, timeout=90)
