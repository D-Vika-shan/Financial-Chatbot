# Financial Data Chatbot

This is a simple chatbot web application built using **Flask** that responds to **predefined financial queries** based on historical data from companies like Apple, Microsoft, and Tesla.

## 🚀 Features

- Interactive web interface to chat with the bot
- Predefined responses based on financial data analysis
- Supports summary, comparison, and data-specific queries
- Stores chat history in the session
- Easily extendable for more financial questions

## 📊 Dataset Used

The chatbot uses a CSV file named `Final Financial Data Analysis.csv` with the following fields:

- Company
- Year
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow from Operating Activities
- Growth % fields for each metric

## 🧠 How the Chatbot Works

1. When a user types a query into the chat window, the chatbot analyzes the message using simple keyword-based matching.
2. If the query matches one of the predefined types, the bot returns relevant data from the CSV.
3. The chat history is stored in Flask's session to persist between page reloads.
4. If the query does not match any known pattern, the bot replies with a default message.

## ✅ Supported Queries (Examples)

- `What is the total revenue for each company?`
- `Show the net income change.`
- `What is the average revenue?`
- `Give me a summary.`
- `What is the revenue growth for Tesla?`
- `Show Microsoft assets growth.`
- `What is the net income growth of Apple?`
- `How much did Tesla's cash flow grow?`
- `Which company had the highest revenue in 2024?`
- `Which company had the lowest net income in 2023?`
- `Compare assets of Apple and Microsoft.`
- `What was the total revenue of Microsoft in 2024?`
- `What was Apple’s net income in 2022?`

## 📁 File Structure

financial-chatbot/
├── app.py
├── Final Financial Data Analysis.csv
├── templates/
│ └── chat.html
└── README.md

## 🛠️ How to Run Locally

1. Install dependencies:

    ```bash
    pip install flask pandas

2. Place Final Financial Data Analysis.csv in the same folder as app.py.

3. Run the Flask app:

    ```bash
    python app.py

4. Open your browser and go to http://127.0.0.1:5000/.

## 🔒 Limitations

- The bot uses hardcoded keyword matching — it cannot understand free-form natural language.
- It only supports queries explicitly coded in the backend.
- It does not learn from data or adapt to new questions.