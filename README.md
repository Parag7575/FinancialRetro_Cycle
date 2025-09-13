# FinancialRetro_Cycle

A retroactive simulation of a balanced investment portfolio in the Indian market, featuring Nifty 50 ETFs and Government Bond ETFs. This project calculates daily returns, moving averages, yield-to-maturity estimates, volatility, Sharpe ratio, and rebalanced portfolio growth over a 10-day period.

---

## 📁 Project Structure

FinancialRetro_Cycle/
│
├── night-cycle.py # Main analysis and simulation script
├── README.md # This file


---

## 🚀 Features

- Simulates a balanced portfolio (70% Nifty 50 ETF & 30% Govt Bond ETF)
- Daily returns and 3-day moving average for Nifty ETF
- Bond YTM estimation (simplified)
- Portfolio cumulative return calculation
- Volatility and Sharpe Ratio computation (annualized)
- Simulated rebalancing with ₹1,00,000 initial capital
- Summary of the final investment state

---

## 📉 Financial Assumptions

| Metric                     | Value              |
|---------------------------|--------------------|
| Initial Portfolio Value   | ₹1,00,000          |
| Risk-Free Rate (Annual)   | 6.5%               |
| Portfolio Allocation      | 70% Nifty / 30% Bond |
| Bond Coupon Rate          | 6.5%               |
| Business Days Simulated   | 10                 |

---

## 📦 Dependencies

This project uses:

- pandas
- numpy

📈 Sample Output
text
Copy code
Extended Night Cycle Retro Calculation Summary (Indian Market):
last_date: 2025-09-13
nifty50_last_close: ₹18050.00
nifty50_return_last_day: 0.002778
nifty50_MA3_last: ₹17990.00
govt_bond_last_close: ₹101.10
govt_bond_return_last_day: 0.001089
govt_bond_ytm_last_estimate: 0.062195
portfolio_last_return: 0.002222
portfolio_cum_return: 1.024872
portfolio_volatility: 0.006176
portfolio_sharpe_ratio: 3.270957
portfolio_value_rebalanced_last: ₹102487.21

🧠 Notes
Designed for educational and backtesting purposes.
Not intended for real-time or production trading systems.
The bond YTM calculation is simplified and assumes 1-year maturity.

🛠️ Future Improvements
Integration with live data APIs (e.g., NSE/BSE)
Longer simulation period
More complex rebalancing logic
Include other asset classes (gold, REITs etc.)

🙋‍♂️ Author
Parag Dutta
