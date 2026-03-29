SELECT
route,
SUM(revenue) AS total_revenue,
SUM(fuel_cost) AS fuel_cost,
SUM(profit) AS profit
FROM route_profitability
GROUP BY route
ORDER BY profit DESC;
