import matplotlib.pyplot as plt
import random

class SmartphoneInventoryAgent:
    def __init__(self, avg_price=600, critical_stock_level=10, discount_threshold=0.2):
        self.avg_price = avg_price
        self.critical_stock_level = critical_stock_level
        self.discount_threshold = discount_threshold
        self.stock = 20
        self.price_history = []
        self.stock_history = []
        self.tobuy_history = []

    def price_monitoring(self):
        # Simulate a random price between 450 and 750
        return random.randint(450, 750)

    def inventory_monitoring(self):
        return self.stock

    def decide_order_quantity(self, price, stock_level):
        discount_price = self.avg_price * (1 - self.discount_threshold)
        tobuy = 0

        if price < discount_price and stock_level >= self.critical_stock_level:
            tobuy = 15  # Price is low and we have enough stock, buy more
        elif stock_level < self.critical_stock_level:
            tobuy = 10  # Stock level is critical, order minimum quantity

        return tobuy

    def order_smartphones(self, tobuy):
        if tobuy > 0:
            self.stock += tobuy

    def run(self, iterations=30):
        for i in range(iterations):
            price = self.price_monitoring()
            stock_level = self.inventory_monitoring()
            tobuy = self.decide_order_quantity(price, stock_level)
            self.order_smartphones(tobuy)

            # Log data for graphing purposes
            self.price_history.append(price)
            self.stock_history.append(stock_level)
            self.tobuy_history.append(tobuy)

            print(f"Iteration {i + 1}: Price = {price}, Stock Level = {stock_level}, Ordered = {tobuy}")

        # Generate graph
        self.plot_data()

    def plot_data(self):
        plt.figure(figsize=(10, 6))

        # Plot price history
        plt.subplot(3, 1, 1)
        plt.plot(self.price_history, label='Price', color='blue')
        plt.axhline(self.avg_price * (1 - self.discount_threshold), color='red', linestyle='--', label='20% Discount Threshold')
        plt.title('Price History')
        plt.xlabel('Iteration')
        plt.ylabel('Price (BDT)')
        plt.legend()

        # Plot stock level history
        plt.subplot(3, 1, 2)
        plt.plot(self.stock_history, label='Stock Level', color='green')
        plt.axhline(self.critical_stock_level, color='red', linestyle='--', label='Critical Stock Level')
        plt.title('Stock Level History')
        plt.xlabel('Iteration')
        plt.ylabel('Stock Level')
        plt.legend()

        # Plot tobuy history
        plt.subplot(3, 1, 3)
        plt.plot(self.tobuy_history, label='Ordered Quantity', color='orange')
        plt.title('Ordered Quantity History')
        plt.xlabel('Iteration')
        plt.ylabel('Ordered Quantity')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    agent = SmartphoneInventoryAgent()
    agent.run()
