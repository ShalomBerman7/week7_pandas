import pandas as pd
import numpy as np


#0
df = pd.read_json('data/orders_simple.json')


#1
def to_datetime(data):
    data['order_date'] = pd.to_datetime(data['order_date'])
    return data


def to_float(df):
    df['total_amount'] = df['total_amount'].str.strip('$').astype(float)
    return df


#2
def del_markings(data):
    data['items_html'] = data['items_html'].str.split('<')
    # data['items_html'] = data['items_html'].str.split('>')
    # data['items_html'] = data['items_html'].str.split('/')
    return data


#3
# df["coupon_used"].fillna("No Coupon", inplace = True)
# m = df['coupon_used'].str.startswith('No Coupon')


#4
def create_month(df):
    df['month'] = (pd.to_datetime(df['order_date'], dayfirst=True)
                  .dt.to_period('M')
                  .groupby(df['order_id'])
                  .rank('dense')
                  .convert_dtypes()
                  )
    return df


#5
def create_order_value_high(df):
    df['high_value_order'] = np.where(df['total_amount'] > df['total_amount'].mean(), True, False)
    return df


def short(df):
    pass

#9
def to_csv(df):
    df.to_csv('clean_orders_212797740.csv',index=False)
