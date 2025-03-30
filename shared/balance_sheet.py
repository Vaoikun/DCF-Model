"""
BalanceSheet class
"""

import numpy as np
import pandas as pd
import yfinance as yf
# import yahoo_fin.stock_info as si: outdated

class BalanceSheet:
    """A BalanceSheet object class. Has a name and a dataframe.

    Attributes:
        name (str): the name of the company.
        df (dataframe): the company's balance sheet data.
    """

    def __init__(self, name, yf_data, start_date="01/01/2019", end_date="12/31/2024"):
        """Sets the name and construct a data frame from the given yfinance object.

            Parameters:
                name (str): the name of the company.
                start_date (str): MM/DD/YYYY
                end_date (str): MM/DD/YYYY
        """
        self.name = name
        self.df = yf_data.balancesheet

    def get_name(self):
        """Returns the name of the company.
        """
        return self.name
    
    def get_bs_df(self):
        """Returns the company's balance sheet.
        """
        return self.df
    
    def get_assets(self):
        return
    
    def get_liability(self):
        return
    
    def get_equity(self):
        return

    def plot_balance_chart(self):
        return
    
if __name__ == "__main__":
    names = ["aapl", "googl", "tsla"]

    for name in names:
        start_date = "01/01/2019"
        end_date = "12/31/2024"

        yf_data = yf.Ticker(name, start=start_date, end=end_date)

        company_bs = BalanceSheet(name, yf_data)
        print("Company's name:", company_bs.get_name())
        print("Company's Balance Sheet:")
        print(company_bs.get_bs_df())
