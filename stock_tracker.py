stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

def track_portfolio():
    total_investment = 0

    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

    print("\nEnter stock name and quantity. Type 'done' to finish.\n")

    while True:
        stock_name = input("Stock name: ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not found in our list. Try again.\n")
            continue

        quantity = int(input("Quantity: "))
        value = stock_prices[stock_name] * quantity
        total_investment += value

        print(f"Added {quantity} shares of {stock_name} (${value})\n")

    print(f"\nTotal Investment: ${total_investment}")

if __name__ == "__main__":
    track_portfolio()
