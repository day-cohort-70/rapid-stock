import os
import sqlite3
from datetime import datetime
from time import time


class TradingService:

    '''A simplified class to buy and sell stock'''

    def __init__(self):
        self.db_path = f"{os.getcwd()}/rapidstock.db"

    def purchase_stock(self, quantity, purchase_price, ticker):
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

            # Write an INSERT INTO statement
            sql_to_execute = """
            INSERT INTO Stocks (
              purchase_date,
              purchase_type,
              purchase_price,
              quantity,
              ticker_symbol
            )
            VALUES ( ?, ?, ?, ?, ? )
            """

            stock_data = ( datetime.now(), "BUY", purchase_price, quantity, ticker )

            c.execute(sql_to_execute, stock_data)
            conn.commit()

        return None

    def sell_stock(self, quantity, market_price, ticker):
        '''Allows a user to sell a stock

        Method arguments
        ----------------
          quantity -- (integer) The number of stocks to purchase
          market_price -- (real) The price of the stock today
        '''
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()

            # Write an INSERT INTO statement
            sql_to_execute = """
            INSERT INTO Stocks (
              purchase_date,
              purchase_type,
              purchase_price,
              quantity,
              ticker_symbol
            )
            VALUES ( ?, ?, ?, ?, ? )
            """

            stock_data = ( datetime.now(), "SELL", market_price, quantity, ticker )

            c.execute(sql_to_execute, stock_data)
            conn.commit()

        return None


    def get_transactions_for_stock(self, ticker):
      """Get all transactions for a single stock

      Args:
          ticker (str): The ticker symbol for a stock
      """
      with sqlite3.connect(self.db_path) as conn:
          conn.row_factory = sqlite3.Row
          c = conn.cursor()

          # Write an INSERT INTO statement
          sql_to_execute = """
          SELECT
            s.purchase_price,
            s.quantity,
            s.purchase_date
          FROM Stocks s
          WHERE
            s.ticker_symbol = ?
          """

          stock_data = ( ticker, )

          c.execute(sql_to_execute, stock_data)
          results = c.fetchall()

          all_transactions = []
          for transaction in results:
              all_transactions.append(dict(transaction))

          return all_transactions



    def get_portfolio(self):
        '''Get all transactions'''


    def clear_database(self):
        '''Deletes all transactions from the database

        Method arguments
        ----------------
          n/a
        '''
        pass


