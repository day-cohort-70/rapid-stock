import os
import sqlite3
from datetime import datetime
from time import time


class TradingService:

    '''A simplified class to buy and sell stock'''

    def __init__(self):
        self.db_path = f"{os.getcwd()}/rapidstock.db"

    def purchase_stock(self, quantity, purchase_price):
        '''Allows a user to purchase a stock

        Add a record to the database table `stocks` with the following columns
          - purchase date
          - type
          - symbol
          - qty
          - price


        Method arguments
        ----------------
          quantity -- (integer) The number of stocks to purchase
          purchase_price -- (real) The price at which the stocks were purchased
        '''
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

        return None

    def sell_stock(self, quantity, market_price):
        '''Allows a user to sell a stock

        Method arguments
        ----------------
          quantity -- (integer) The number of stocks to purchase
          market_price -- (real) The price of the stock today
        '''
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

        return None


    def get_transactions_for_stock(self, ticker):
      """Get all transactions for a single stock

      Args:
          ticker (str): The ticker symbol for a stock
      """

    def get_portfolio(self):
        '''Get all transactions'''


    def clear_database(self):
        '''Deletes all transactions from the database

        Method arguments
        ----------------
          n/a
        '''
        pass


amz = TradingService()

