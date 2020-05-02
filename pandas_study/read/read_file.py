import pandas as pd


def read_excel():
    df = pd.read_excel('ex1.xls', sheet_name='Sheet1')
    df1 = pd.read_excel('ex1.xls', sheet_name='Sheet1', names=['name', 'age'])
    print(df)
    print(df1)
    df.to_csv('exl.csv')
    # df_csv = pd.read_csv('ex1.csv')
    # print(df_csv)



if __name__ == '__main__':
    read_excel()
