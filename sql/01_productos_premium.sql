-- Productos premium (precio de venta > 100), los 100 más caros
-- Fuente: dataset público thelook_ecommerce (BigQuery)
SELECT name, category, brand, cost, retail_price
FROM `bigquery-public-data.thelook_ecommerce.products`
WHERE retail_price > 100
ORDER BY retail_price DESC
LIMIT 100;
