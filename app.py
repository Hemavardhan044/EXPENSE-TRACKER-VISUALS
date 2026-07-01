import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("💰 Expense Tracker")

# Read CSV File
df = pd.read_csv("expenses.csv")

# Display Data
st.subheader("Expense Records")
st.dataframe(df)

# Expense Form
st.subheader("Add New Expense")

with st.form("expense_form"):

    date = st.date_input("Date")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transport",
            "Shopping",
            "Entertainment"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    submit = st.form_submit_button(
        "Add Expense"
    )

# Save Expense
if submit:

    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount],
        "Description": [description]
    })

    df = pd.concat(
        [df, new_expense],
        ignore_index=True
    )

    df.to_csv(
        "expenses.csv",
        index=False
    )

    st.success("Expense Added Successfully!")

# Total Expense
total = df["Amount"].sum()

st.metric(
    "Total Expense",
    f"₹{total:,.2f}"
)

# Category Summary
category_total = df.groupby(
    "Category"
)["Amount"].sum()

st.subheader("Category Summary")

st.write(category_total)

# Bar Chart
st.subheader("Bar Chart")

fig1, ax1 = plt.subplots()

category_total.plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel("Category")
ax1.set_ylabel("Amount")

st.pyplot(fig1)

# Pie Chart
st.subheader("Pie Chart")

fig2, ax2 = plt.subplots()

category_total.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

ax2.set_ylabel("")

st.pyplot(fig2)

# Budget Alert
budget = 5000

if total > budget:

    st.error("⚠ Budget Exceeded!")

else:

    st.success("✅ Within Budget")

# Create Reports Folder
if not os.path.exists("reports"):
    os.makedirs("reports")

# Export Excel Report
if st.button("Export Report"):

    report_path = "reports/expense_report.xlsx"

    with pd.ExcelWriter(
        report_path,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Expenses",
            index=False
        )

        category_total.to_frame().to_excel(
            writer,
            sheet_name="Category Summary"
        )

    st.success(
        "Report Exported Successfully!"
    )