from client import PriceMonitorClient
def main():
    c = PriceMonitorClient()
    print(c.monitor_prices("SKU-001", 100.0, 125.0, [119.99, 122.50]))
if __name__ == '__main__':
    main()
