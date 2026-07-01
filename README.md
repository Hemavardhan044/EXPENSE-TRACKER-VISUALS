# 💰 Expense Tracker with Visualizations

## Overview

This project is a simple **Expense Tracker** built using **Python**, **Pandas**, **Matplotlib**, and **Tkinter/Streamlit**. It helps users record expenses, analyze spending by category, visualize data using charts, and export reports to Excel.

## Features

- Add expenses manually or upload a CSV file
- Categorize and clean expense data
- View category-wise and date-wise expense summaries
- Generate pie and bar charts
- Set a monthly budget and receive alerts
- Export reports to Excel

## Technologies Used

- Python
- Pandas
- Matplotlib
- Tkinter or Streamlit
- OpenPyXL

## Project Structure

```
Expense-Tracker/
│── app.py
│── data/
│   └── expenses.csv
│── reports/
│   └── expense_report.xlsx
│── requirements.txt
│── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Run the application.

For Tkinter:

```bash
python app.py
```

For Streamlit:

```bash
streamlit run app.py
```

## Sample CSV Format

| Date | Category | Description | Amount |
|------|----------|-------------|-------:|
| 2026-06-01 | Food | Lunch | 250 |
| 2026-06-02 | Transport | Bus | 60 |
| 2026-06-03 | Shopping | Clothes | 1500 |

## Output

- Expense Dashboard
- Pie Chart
- Bar Chart
- Budget Alerts
- Excel Report

## Future Improvements

- User Login
- Interactive Charts
- PDF Report Export
- Monthly Expense Prediction

## License

This project is for educational purposes.
