# ETL Sales Pipeline

## 🔹 Descrição do Projeto
O **ETL Sales Pipeline** é um projeto que automatiza o **processamento de dados de vendas**. Ele realiza o fluxo completo de **ETL (Extract, Transform, Load)** e permite análise rápida das vendas.  

O pipeline é implementado em **Python**, utilizando **pandas** para manipulação de dados, **SQLite** para armazenamento local e **PostgreSQL** (opcional) para armazenamento corporativo.

---

## 🔹 Funcionalidades do Pipeline
1. **Geração de dados de exemplo:**  
   - Cria um CSV (`sales_data.csv`) com vendas fictícias de produtos como Laptop, Mouse, Keyboard e Monitor.  

2. **Extract (Extração):**  
   - Lê os dados do CSV gerado.  

3. **Transform (Transformação):**  
   - Remove valores nulos;  
   - Converte datas para formato datetime;  
   - Calcula a coluna `total_sales` (`quantity * price`);  
   - Agrega vendas por produto para análise.  

4. **Load (Carga):**  
   - Armazena os dados transformados em **SQLite** (`sales.db`) em duas tabelas:  
     - `sales_raw` (dados detalhados)  
     - `sales_aggregated` (dados agregados por produto)  
   - Suporte para **PostgreSQL** caso configurado.  

5. **Análise de dados com SQL:**  
   - Total de vendas por produto;  
   - Vendas médias por data;  
   - Mostra os resultados no console.
<img width="453" height="181" alt="Captura de Tela 2025-11-15 às 17 16 45" src="https://github.com/user-attachments/assets/84f76442-fffb-4093-a208-ae8a55faef97" />

