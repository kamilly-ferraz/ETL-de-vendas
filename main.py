import pandas as pd
import sqlite3
import os
from datetime import datetime

def generate_sample_data(file_path='sales_data.csv'):
    if not os.path.exists(file_path):
        data = {
            'order_id': [1, 2, 3, 4, 5],
            'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor'],
            'quantity': [1, 2, 1, None, 3],
            'price': [1200.50, 25.00, 45.99, 1200.50, 150.00],
            'order_date': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19']
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        print(f"Arquivo de exemplo '{file_path}' gerado.")

def extract_data(file_path='sales_data.csv'):
    print("Extraindo dados...")
    df = pd.read_csv(file_path)
    return df

def transform_data(df):
    print("Transformando dados...")
    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_sales'] = df['quantity'] * df['price']
    aggregated = df.groupby('product').agg({'total_sales': 'sum'}).reset_index()
    return df, aggregated

def load_data(df, aggregated, db_name='sales.db'):
    print("Carregando dados no banco...")
    conn = sqlite3.connect(db_name)
    df.to_sql('sales_raw', conn, if_exists='replace', index=False)
    aggregated.to_sql('sales_aggregated', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Dados carregados em '{db_name}'.")

def analyze_data(db_name='sales.db'):
    print("Analisando dados com SQL...")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT product, SUM(quantity * price) AS total_sales
        FROM sales_raw
        GROUP BY product
        ORDER BY total_sales DESC;
    """)
    results1 = cursor.fetchall()
    print("\nTotal de vendas por produto:")
    for row in results1:
        print(row)
    
    cursor.execute("""
        SELECT order_date, AVG(total_sales) AS avg_sales
        FROM (
            SELECT order_date, quantity * price AS total_sales
            FROM sales_raw
        )
        GROUP BY order_date;
    """)
    results2 = cursor.fetchall()
    print("\nVendas médias por data:")
    for row in results2:
        print(row)
    
    conn.close()

if __name__ == "__main__":
    generate_sample_data()
    df = extract_data()
    df_transformed, aggregated = transform_data(df)
    load_data(df_transformed, aggregated)
    analyze_data()
