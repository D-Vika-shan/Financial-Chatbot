from flask import Flask, request, render_template, session, redirect, url_for
import pandas as pd


app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load financial data
df = pd.read_csv("Final Financial Data Analysis.csv")

# Basic chatbot logic
def simple_chatbot(query):
    query = query.lower()

    if "total revenue" in query:
        total = df.groupby("Company")["Total Revenue"].sum()
        return f"{total.to_string()}"

    elif "net income change" in query or ("net income" in query and "change" in query):
        changes = df[["Company", "Year", "Net Income Growth %"]].dropna().tail(6)
        return f"{changes.to_string(index=False)}"

    elif "average revenue" in query:
        avg = df.groupby("Company")["Total Revenue"].mean()
        return f"Average Total Revenue:\n{avg.to_string()}"

    elif "summary" in query:
        return (
            "Summary:\n"
            "- Microsoft shows strong financial growth.\n"
            "- Apple leads in net income but should watch liabilities.\n"
            "- Tesla is growing assets steadily.\n"
        )
    
    elif "revenue growth" in query and "tesla" in query:
        tesla = df[df["Company"] == "Tesla"][["Year", "Total Revenue Growth %"]].dropna()
        return f"Tesla Revenue Growth (%):\n{tesla.to_string(index=False)}"

    elif "assets growth" in query and "microsoft" in query:
        msft = df[df["Company"] == "Microsoft"][["Year", "Total Assets Growth %"]].dropna()
        return f"Microsoft Assets Growth (%):\n{msft.to_string(index=False)}"

    elif "net income growth" in query and "apple" in query:
        apple = df[df["Company"] == "Apple"][["Year", "Net Income Growth %"]].dropna()
        return f"Apple Net Income Growth (%):\n{apple.to_string(index=False)}"

    elif "cash flow growth" in query and "tesla" in query:
        tesla = df[df["Company"] == "Tesla"][["Year", "Cash Flow from Operating Activities Growth %"]].dropna()
        return f"Tesla Cash Flow Growth (%):\n{tesla.to_string(index=False)}"

    elif "highest revenue" in query and "2024" in query:
        max_rev = df[df["Year"] == 2024].sort_values("Total Revenue", ascending=False).iloc[0]
        return f"Highest revenue in 2024: {max_rev['Company']} with {max_rev['Total Revenue']}"

    elif "lowest net income" in query and "2023" in query:
        min_income = df[df["Year"] == 2023].sort_values("Net Income", ascending=True).iloc[0]
        return f"Lowest Net Income in 2023: {min_income['Company']} with {min_income['Net Income']}"

    elif "compare assets" in query and "apple" in query and "microsoft" in query:
        apple_assets = df[(df["Company"] == "Apple")][["Year", "Total Assets"]]
        msft_assets = df[(df["Company"] == "Microsoft")][["Year", "Total Assets"]]
        return (
            f"Apple Assets:\n{apple_assets.to_string(index=False)}\n\n"
            f"Microsoft Assets:\n{msft_assets.to_string(index=False)}"
        )

    elif "microsoft" in query and "2024" in query and "total revenue" in query:
        value = df[(df["Company"] == "Microsoft") & (df["Year"] == 2024)]["Total Revenue"].values
        return f"Microsoft's total revenue in 2024 was {value[0]}" if len(value) > 0 else "Data not found."

    elif "apple" in query and "net income" in query and "2022" in query:
        value = df[(df["Company"] == "Apple") & (df["Year"] == 2022)]["Net Income"].values
        return f"Apple's net income in 2022 was {value[0]}" if len(value) > 0 else "Data not found."

    elif "i'm sorry" in query:
        return "No worries. You can ask me about financial data like revenue, income, growth, etc."

    else:
        return "I'm sorry, I can only respond to predefined financial queries. Try asking about revenue, net income, or growth."

@app.route("/", methods=["GET", "POST"])
def chat():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_msg = request.form["message"]
        bot_reply = simple_chatbot(user_msg)

        # Save messages
        session["chat_history"].append({"sender": "user", "text": user_msg})
        session["chat_history"].append({"sender": "bot", "text": bot_reply})
        session.modified = True

        return redirect(url_for("chat"))

    return render_template("chat.html", chat_history=session["chat_history"])

@app.route("/reset")
def reset():
    session.pop("chat_history", None)
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True)
