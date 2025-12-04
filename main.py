from utils import df, to_datetime, to_float, del_markings, create_month, create_order_value_high, to_csv


print(df.info())
if __name__ == '__main__':
    
    to_datetime(df)
    to_float(df)
    del_markings(df)
    to_csv(df)
    create_month(df)
    create_order_value_high(df)

print(df.info())
