import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:password@localhost:5432/fleetdb")

deliveries = pd.read_csv("../data/deliveries.csv")
fuel = pd.read_csv("../data/fuel_logs.csv")
drivers = pd.read_csv("../data/drivers.csv")
maintenance = pd.read_csv("../data/maintenance.csv")

fuel_summary = fuel.groupby("truck_id").sum().reset_index()

merged = deliveries.merge(fuel_summary, on="truck_id")

merged["cost_per_mile"] = merged["fuel_cost"] / merged["miles"]
merged["profit"] = merged["revenue"] - merged["fuel_cost"]

deliveries.to_sql("deliveries", engine, if_exists="replace", index=False)
fuel.to_sql("fuel_logs", engine, if_exists="replace", index=False)
drivers.to_sql("drivers", engine, if_exists="replace", index=False)
maintenance.to_sql("maintenance", engine, if_exists="replace", index=False)
merged.to_sql("route_profitability", engine, if_exists="replace", index=False)

print("Pipeline complete")
