import pandas as pd
import numpy as np

# Sample historic price data for Indian Nifty 50 ETF and Govt Bond ETF
data = {
    'date': pd.date_range(start='2025-09-01', periods=10, freq='B'),  # 10 business days
    'nifty50_etf_close': [17500, 17600, 17750, 17650, 17800, 17900, 17950, 17920, 18000, 18050],
    'govt_bond_etf_close': [100, 100.25, 100.5, 100.4, 100.6, 100.7, 100.9, 100.85, 101.0, 101.1],
    'govt_bond_coupon': 0.065  # 6.5% annual coupon yield in decimal
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Calculate daily returns for Nifty ETF and Govt Bond ETF
df['nifty50_return'] = df['nifty50_etf_close'].pct_change()
df['govt_bond_return'] = df['govt_bond_etf_close'].pct_change()

# Calculate 3-day moving average for Nifty ETF closing price
df['nifty50_MA3'] = df['nifty50_etf_close'].rolling(window=3).mean()

# More realistic bond yield to maturity estimate (approximate)
# Assume Face Value = ₹100, maturity ~ 1 year (simplification)
face_value = 100
maturity_years = 1
coupon_payment = data['govt_bond_coupon'] * face_value  # annual coupon in ₹

def estimate_ytm(price):
    return (coupon_payment + (face_value - price) / maturity_years) / ((face_value + price) / 2)

df['govt_bond_ytm_estimate'] = df['govt_bond_etf_close'].apply(estimate_ytm)

# Portfolio allocation: 70% Nifty ETF, 30% Govt Bond ETF (common balanced allocation in India)
target_alloc = {'nifty50': 0.7, 'govt_bond': 0.3}

# Calculate daily portfolio return based on allocation
df['portfolio_return'] = (df['nifty50_return'] * target_alloc['nifty50'] +
                          df['govt_bond_return'] * target_alloc['govt_bond'])

# Calculate portfolio cumulative return (starting from 1)
df['portfolio_cum_return'] = (1 + df['portfolio_return'].fillna(0)).cumprod()

# Portfolio volatility (standard deviation of daily returns)
portfolio_volatility = df['portfolio_return'].std()

# Assume Indian risk-free rate ~6.5% annual (based on G-sec yields)
risk_free_rate_annual = 0.065
risk_free_rate_daily = (1 + risk_free_rate_annual) ** (1/252) - 1

# Excess returns (portfolio return - risk-free rate)
df['excess_return'] = df['portfolio_return'] - risk_free_rate_daily

# Sharpe ratio (annualized)
sharpe_ratio = (df['excess_return'].mean() / portfolio_volatility) * np.sqrt(252)

# Basic portfolio rebalancing simulation with initial portfolio value ₹1,00,000
portfolio_value = 100000
portfolio_values = []
weights = target_alloc.copy()

for i, row in df.iterrows():
    if i == df.index[0]:
        portfolio_values.append(portfolio_value)
    else:
        daily_return = (weights['nifty50'] * row['nifty50_return'] +
                        weights['govt_bond'] * row['govt_bond_return'])
        portfolio_value *= (1 + (daily_return if not pd.isna(daily_return) else 0))
        weights = target_alloc.copy()
        portfolio_values.append(portfolio_value)

df['portfolio_value_rebalanced'] = portfolio_values

# Night cycle report summary with Indian context
night_cycle_summary = {
    'last_date': df.index[-1],
    'nifty50_last_close': df['nifty50_etf_close'].iloc[-1],
    'nifty50_return_last_day': df['nifty50_return'].iloc[-1],
    'nifty50_MA3_last': df['nifty50_MA3'].iloc[-1],
    'govt_bond_last_close': df['govt_bond_etf_close'].iloc[-1],
    'govt_bond_return_last_day': df['govt_bond_return'].iloc[-1],
    'govt_bond_ytm_last_estimate': df['govt_bond_ytm_estimate'].iloc[-1],
    'portfolio_last_return': df['portfolio_return'].iloc[-1],
    'portfolio_cum_return': df['portfolio_cum_return'].iloc[-1],
    'portfolio_volatility': portfolio_volatility,
    'portfolio_sharpe_ratio': sharpe_ratio,
    'portfolio_value_rebalanced_last': df['portfolio_value_rebalanced'].iloc[-1]
}

print("Extended Night Cycle Retro Calculation Summary (Indian Market):")
for k, v in night_cycle_summary.items():
    if isinstance(v, float):
        # Currency values: show with ₹ symbol and 2 decimal places if applicable
        if 'close' in k or 'value' in k:
            print(f"{k}: ₹{v:.2f}")
        else:
            print(f"{k}: {v:.6f}")
    else:
        print(f"{k}: {v}")
