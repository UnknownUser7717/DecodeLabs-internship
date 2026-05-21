USE DecodelabsDB;


BULK INSERT Orders
FROM 'D:\files\Code\DecodeLabs-internship\Data\cleaned_dataset.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);

SELECT TOP 5 * FROM Orders;
