# Monte Carlo Option Pricing

This Python script calculates the option price using the Monte Carlo method. It provides a simple yet effective way to estimate option prices based on various input parameters.

## Usage

1. Make sure you have Python and NumPy installed on your system.
2. Run the script in your terminal or Python environment.
3. Enter the required parameters such as stock price, strike price, time to expiration, risk-free interest rate, volatility, and option type (call or put).
4. The script will calculate and display the option price.

## Parameters

- `S`: Current stock price.
- `K`: Strike price.
- `T`: Time to expiration (in years).
- `r`: Risk-free interest rate.
- `sigma`: Volatility of the underlying asset.
- `option_type`: Type of option ('call' for call option, 'put' for put option).
- `num_simulations`: Number of Monte Carlo simulations (default is 10,000).

## Example

Here's an example of how to use the script:

```python
python monte_carlo_option_pricing.py
Enter current stock price: 100
Enter strike price: 110
Enter time to expiration (in years): 1
Enter risk-free interest rate: 0.05
Enter volatility: 0.2
Enter option type (call/put): call
Option Price: 8.07


## License 
MIT
