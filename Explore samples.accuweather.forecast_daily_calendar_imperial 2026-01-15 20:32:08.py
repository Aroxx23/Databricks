# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT date, temperature_max, temperature_min, precipitation_probability
# MAGIC FROM `samples`.`accuweather`.`forecast_daily_calendar_imperial`
# MAGIC ORDER BY date DESC
# MAGIC LIMIT 10;
