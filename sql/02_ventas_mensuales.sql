-- Pedidos e ingresos por mes (se excluyen pedidos cancelados y devueltos)
-- Fuente: dataset público thelook_ecommerce (BigQuery)
SELECT
  DATE_TRUNC(DATE(created_at), MONTH) AS mes,
  COUNT(DISTINCT order_id) AS pedidos,
  ROUND(SUM(sale_price), 2) AS ingresos
FROM `bigquery-public-data.thelook_ecommerce.order_items`
WHERE status NOT IN ('Cancelled', 'Returned')
GROUP BY mes
ORDER BY mes;
