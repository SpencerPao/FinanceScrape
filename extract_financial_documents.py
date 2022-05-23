#!/usr/bin/env python3
"""
This is a script that will scrape financial information.
I will be using the website: https://financialmodelingprep.com/developer/
Free plan!
    Upside: More accessbile and more open to other competitiors such as Yahoo
    Downside: 250 requests per day
    Upgrade with a plan
    Provides equations to how they configured their ratios and statistics
        Other websites are not as transparent.
Includes: Income Statements / Balance Sheets / Cash Flow Statements
          Statistics

Parameter specification: (unless specified otherwise)
    ticker -> Company stock name
    limit -> Number of records per entry you'd like.
    key -> API key that was generated for you when you create an account
    period -> annual or quarter
"""
import Financial_Data_Scraping as fds
import pandas as pd
if __name__ == "__main__":
    """Running the scraper to obtain financial data."""
    key = pd.read_csv('key.txt', header=None)[0][0]
    tickers = pd.read_csv('tickers.txt', header=None)[0]
    for t in tickers:
        IS = fds.get_income_statement(ticker=t, limit=6, key=key, period='annual')
        BS = fds.get_balance_sheet(ticker=t, limit=6, key=key, period='annual')
        CF = fds.get_cash_flow_statement(ticker=t, limit=6, key=key, period='annual')
        FR = fds.get_financial_ratios(ticker=t, limit=6, key=key, period='annual')
        KM = fds.get_key_metrics(ticker=t, limit=6, key=key, period='annual')
        P = fds.get_daily_prices(ticker=t, timeseries=5*261, key=key)
        EV = fds.get_enterprise_value(ticker=t, rate=5*261, key=key, period='annual')
        # Creating a writer
        writer = pd.ExcelWriter('{}.xlsx'.format(t), engine='xlsxwriter')
        # Putting into excel file.
        IS.to_excel(writer, sheet_name='Income Statement')
        BS.to_excel(writer, sheet_name='Balance Sheet Statement')
        CF.to_excel(writer, sheet_name='Cash Flow Statement')
        FR.to_excel(writer, sheet_name='Financial Ratios')
        KM.to_excel(writer, sheet_name='Key Metrics')
        P.to_excel(writer, sheet_name='Daily Prices')
        EV.to_excel(writer, sheet_name='Enterprise Value')
        # Saving the writer.
        writer.save()
        print('Finished with :', t)
