import numpy as np

def monte_carlo_option_price(S, K, T, r, sigma, option_type='call', num_simulations=10000):
    """
    Calculate the option price using the Monte Carlo method.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    T (float): Time to expiration (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    option_type (str): 'call' for call option, 'put' for put option
    num_simulations (int): Number of Monte Carlo simulations

    Returns:
    option_price (float): Option price
    """
    
    dt = T / 252  # Assuming 252 trading days in a year
    option_prices = []
    
    for _ in range(num_simulations):
        z = np.random.standard_normal()
        S_T = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        
        if option_type == 'call':
            option_payoff = max(0, S_T - K)
        elif option_type == 'put':
            option_payoff = max(0, K - S_T)
        
        option_prices.append(option_payoff * np.exp(-r * T))
    
    option_price = np.mean(option_prices)
    
    return option_price

if __name__ == "__main__":
    S0 = float(input("Enter current stock price: "))
    K = float(input("Enter strike price: "))
    T = float(input("Enter time to expiration (in years): "))
    r = float(input("Enter risk-free interest rate: "))
    sigma = float(input("Enter volatility: "))
    option_type = input("Enter option type (call/put): ").lower()
    
    option_price = monte_carlo_option_price(S0, K, T, r, sigma, option_type)
    
    print(f'Option Price: {option_price:.2f}')

