USE DecodelabsDB;


BULK INSERT Orders
FROM 'C:\Users\donia\PycharmProjects\PythonProject\DecodeLabs-internship\Data\cleaned_dataset.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);

SELECT TOP 5 * FROM Orders;
