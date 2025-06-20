# 🧠 Amazon Sales AI Agent

An interactive AI-powered data analyst built with LangChain and OpenAI. It answers natural language questions using analysis tools applied to real Amazon sales data (2019–2024).

---

## 🔍 Example Questions

- “What is the monthly revenue trend?”
- “Show me the top 5 products by sales”
- “What’s the average profit by region?”
- “Plot product category distribution”
- “How many orders were cancelled or returned?”

---

## 📊 Dataset Summary

Dataset includes Amazon sales data from 2019 to 2024, with fields such as:

- `order_date`
- `product_name`
- `product_category`
- `region`
- `quantity_sold`
- `unit_price`
- `total_sales`
- `profit_margin`
- `order_status`
- `payment_method`

📁 Cleaned file: `data/clean_amazon_sales.csv`

---

## 🧩 Features

| Feature                      | Description                              |
|-----------------------------|------------------------------------------|
| 📈 Revenue Trends            | Aggregates monthly sales                 |
| 🏆 Top Products              | Identifies bestsellers by revenue        |
| 🌍 Regional Profit Insights  | Computes average profit by region        |
| 📊 Visualizations            | Generates plots and pie charts           |
| 🧠 LangChain Agent           | Interprets and responds to natural queries |

---

## 🛠 Tech Stack

- **LangChain** – AI agent framework  
- **OpenAI GPT-4** – Language model  
- **Pandas** – Data manipulation  
- **Matplotlib** – Visualization  
- **Jupyter Notebook** – Interactive testing

---

## 🚀 How to Run the Project

### 🔧 Install dependencies

```bash
git clone https://github.com/YOUR_USERNAME/amazon-sales-agent.git
cd amazon-sales-agent

python3 -m venv venv
source venv/bin/activate     # On Windows: .\venv\Scripts\activate

pip install -r requirements.txt

