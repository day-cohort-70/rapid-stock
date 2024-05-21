from broker import TradingService

# Create instance of Rapid Stock trading service
rapid = TradingService()

# Buy some stocks
# rapid.purchase_stock(1000.25, 256.0, "MSFT")
# rapid.purchase_stock(765.333, 1300.0, "AMZN")
# rapid.purchase_stock(987.0, 86.0, "LYFT")
# rapid.purchase_stock(45.5, 673.0, "APPL")
# rapid.purchase_stock(4512.666666, 23.0, "F")
# rapid.purchase_stock(1000.25, 256.0, "MSFT")
# rapid.purchase_stock(765.333, 1300.0, "AMZN")
# rapid.purchase_stock(987.0, 86.0, "LYFT")
# rapid.purchase_stock(45.5, 673.0, "APPL")
# rapid.purchase_stock(4512.666666, 23.0, "F")

# Sell some stocks
# rapid.sell_stock(500, 29.0, "F")


# Get purchases for a single stock
rapid.get_transactions_for_stock("LYFT")

# Get entire portfolio and calculate total value


# MARKET CRASH!! Client liquidates their entire account and cancels service.

