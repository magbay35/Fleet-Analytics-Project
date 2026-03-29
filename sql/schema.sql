CREATE TABLE deliveries (
    delivery_id INT,
    truck_id TEXT,
    route TEXT,
    client TEXT,
    revenue NUMERIC,
    miles INT
);

CREATE TABLE fuel_logs (
    truck_id TEXT,
    date DATE,
    fuel_gallons NUMERIC,
    fuel_cost NUMERIC
);

CREATE TABLE drivers (
    driver_id TEXT,
    truck_id TEXT,
    driver_name TEXT,
    idle_hours NUMERIC
);

CREATE TABLE maintenance (
    truck_id TEXT,
    last_service_days INT,
    engine_hours INT
);
