USE DecodelabsDB;


-- BULK INSERT Orders
-- FROM 'D:\files\Code\DecodeLabs-internship\Data\cleaned_dataset.csv'
-- WITH (
--     FIELDTERMINATOR = ',',
--     ROWTERMINATOR = '\n',
--     FIRSTROW = 2,
--     TABLOCK
-- );

SELECT TOP 5 * FROM Orders;

SELECT Product, ROUND(SUM(TotalPrice), 2) AS TotalSales
FROM Orders
GROUP BY Product
ORDER BY TotalSales DESC;

SELECT OrderStatus, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY OrderStatus
ORDER BY TotalOrders DESC;

SELECT ReferralSource, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue
FROM Orders
GROUP BY ReferralSource
ORDER BY AvgOrderValue DESC;

SELECT Product, ROUND(SUM(TotalPrice), 2) AS TotalSales
FROM Orders
GROUP BY Product
HAVING SUM(TotalPrice) > 300000
ORDER BY TotalSales DESC;

SELECT PaymentMethod, ROUND(AVG(UnitPrice), 2) AS AvgUnitPrice
FROM Orders
GROUP BY PaymentMethod
HAVING AVG(UnitPrice) > 350
ORDER BY AvgUnitPrice DESC;

SELECT Product, OrderStatus, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY Product, OrderStatus
ORDER BY Product ASC, TotalOrders DESC;

SELECT PaymentMethod, ROUND(sum(TotalPrice), 2) AS TotalRevenue
from Orders
group by PaymentMethod
having COUNT(*) > 200
order by TotalRevenue desc;
