import pandas as pd

dataframe = pd.read_csv(r'C:\Users\karan\Desktop\Practice\stocks project\NIFTY50.csv')

stocks = pd.DataFrame(dataframe)
print(stocks)

rows_with_nulls = stocks[stocks.isna().any(axis=1)]
print("\nRows with null values:")
# print(rows_with_nulls)

print(stocks.info())

# # Convert 'Date' to datetime with the specific format
# stocks['Date '] = pd.to_datetime(stocks['Date '], format='%d-%b-%Y')

# # Check for invalid dates (those that could not be parsed)
# invalid_dates = stocks[stocks['Date '].isna()]
# print("Invalid dates:")
# print(invalid_dates)
# # Display the DataFrame after conversion
# print("\nDataFrame after converting the 'Date' column:")
# print(stocks)

stocks.rename(columns={'Turnover (₹ Cr)': 'Turnover'}, inplace=True)

print(stocks)
duplicate_columns = stocks.columns[stocks.columns.duplicated()].tolist()
if duplicate_columns:
    # Drop the duplicate column
    stocks = stocks.loc[:, ~stocks.columns.duplicated()]

print(stocks)
stocks.to_csv(r'C:\Users\karan\Desktop\Practice\stocks project\NIFTY50.csv')