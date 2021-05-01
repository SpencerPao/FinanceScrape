#!/usr/bin/env python3
"""This houses all the important functions that are called in the script."""
import pandas as pd
import requests


def get_income_statement(ticker, limit, key, period):
    """Get the Income Statement."""
    URL = 'https://financialmodelingprep.com/api/v3/income-statement/'
    try:
        r = requests.get(
            '{}{}?period={}?limit={}&apikey={}'.format(URL,
                                                       ticker,
                                                       period,
                                                       limit,
                                                       key))
        incomeStatement = pd.DataFrame.from_dict(r.json()).transpose()
        incomeStatement.columns = incomeStatement.iloc[0]
        return incomeStatement[1:]
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Income statement sheet ERROR: ', str(e))


def get_balance_sheet(ticker, limit, key, period):
    """Get the Balance sheet."""
    URL = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        balanceSheet = pd.DataFrame.from_dict(r.json()).transpose()
        balanceSheet.columns = balanceSheet.iloc[0]
        return balanceSheet[1:]
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Balance sheet statement ERROR: ', str(e))


def get_cash_flow_statement(ticker, limit, key, period):
    """Get the Cash flow statements."""
    URL = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        cashFlow = pd.DataFrame.from_dict(r.json()).transpose()
        cashFlow.columns = cashFlow.iloc[0]
        return cashFlow[1:]
    except requests.exceptions.HTTPError as e:
        print('Requesting Cash flow statement ERROR: ', str(e))


def get_financial_ratios(ticker, limit, key, period):
    """Period is ttm | annual | quarter."""
    URL = 'https://financialmodelingprep.com/api/v3/'
    if period == "ttm":
        try:
            r = requests.get(
                '{}/ratios-ttm/{}?{}&apikey={}'.format(URL,
                                                       ticker,
                                                       period,
                                                       key))
            fr = pd.DataFrame.from_dict(r.json()).transpose()
            fr.columns = [ticker + " TTM Ratios"]
            return fr
        except requests.exceptions.HTTPError as e:
            print('Requesting Financial ratios ERROR(1): ', str(e))
    elif period == "annual" or period == "quarter":
        try:
            r = requests.get(
                '{}ratios/{}?period={}&?limit={}&apikey={}'.format(URL,
                                                                   ticker,
                                                                   period,
                                                                   limit,
                                                                   key))
            fr = pd.DataFrame.from_dict(r.json()).transpose()
            fr.columns = fr.iloc[1]
            return fr[2:]
        except requests.exceptions.HTTPError as e:
            print('Requesting Financial ratios ERROR(2): ', str(e))
    else:
        print('ERROR: Define the period you want: ttm | annual | quarter')
        return None


def get_key_metrics(ticker, limit, key, period):
    """Period is ttm | annual | quarter."""
    URL = 'https://financialmodelingprep.com/api/v3/'
    if period == "ttm":
        try:
            r = requests.get(
                '{}key-metrics-ttm/{}?apikey={}'.format(URL, ticker, key))
            km = pd.DataFrame.from_dict(r.json()).transpose()
            km.columns = [ticker + " TTM Ratios"]
            return km
        except requests.exceptions.HTTPError as e:
            print('Requesting Key Metrics ERROR(1): ', str(e))
    elif period == "annual" or period == "quarter":
        try:
            r = requests.get(
                '{}key-metrics/{}?period={}&?limit={}&apikey={}'.format(URL,
                                                                        ticker,
                                                                        period,
                                                                        limit,
                                                                        key))
            km = pd.DataFrame.from_dict(r.json()).transpose()
            km.columns = km.iloc[1]
            return km[2:]
        except requests.exceptions.HTTPError as e:
            print('Requesting Key Metrcs ERROR(2): ', str(e))
    else:
        print('ERROR: Define the period you want: ttm | annual | quarter')
        return None


def get_daily_prices(ticker, timeseries, key):
    """Parameter: timeseries in this case is the number of days."""
    URL = 'https://financialmodelingprep.com/api/v3/historical-price-full/'
    try:
        r = requests.get('{}{}?timeseries={}&apikey={}'.format(URL,
                                                               ticker,
                                                               timeseries,
                                                               key))
        return pd.DataFrame.from_dict(r.json())['historical'].apply(pd.Series)
    except requests.exceptions.HTTPError as e:
        print('Requesting daily Prices ERROR: ', str(e))


def get_enterprise_value(ticker, rate, key, period):
    """Period is annual or quarter. The rate is the number of days."""
    URL = 'https://financialmodelingprep.com/api/v3/enterprise-values/'
    try:
        r = requests.get('{}{}?period={}&limit={}&apikey={}'.format(URL,
                                                                    ticker,
                                                                    period,
                                                                    rate,
                                                                    key))
        return pd.DataFrame.from_dict(r.json())
    except requests.exceptions.HTTPError as e:
        print('Requesting Enterprise Value ERROR: ', str(e))
