USE DecodelabsDB;

CREATE TABLE Orders (
    OrderID VARCHAR(10),
    Date DATE,
    Year INT,
    Month INT,
    CustomerID VARCHAR(10),
    Product VARCHAR(20),
    Quantity INT,
    UnitPrice FLOAT,
    ShippingAddress VARCHAR(10),
    PaymentMethod VARCHAR(20),
    OrderStatus VARCHAR(20),
    TrackingNumber VARCHAR(20),
    ItemsInCart INT,
    CouponCode VARCHAR(20),
    ReferralSource VARCHAR(20),
    TotalPrice FLOAT
);

BULK INSERT Orders
FROM 'C:\Users\donia\PycharmProjects\PythonProject\DecodeLabs-internship\Data\cleaned_dataset.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);

SELECT TOP 5 * FROM Orders;