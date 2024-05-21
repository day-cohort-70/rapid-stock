CREATE TABLE Stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date TIMESTAMP NOT NULL,
    purchase_type VARCHAR(4) NOT NULL,
    ticker_symbol VARCHAR(10) NOT NULL,
    quantity FLOAT NOT NULL,
    purchase_price FLOAT NOT NULL
);

