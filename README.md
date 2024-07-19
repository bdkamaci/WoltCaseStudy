# Wolt Backend Intern Position Case Study

## Overview

This repository contains the code for the backend implementation of a delivery fee calculation system for Wolt. 
The system calculates the delivery fee based on various factors such as cart value, delivery distance, number of items, and the time of the delivery request.

## Files

### `main.py`

This file contains the main implementation of the delivery fee calculation system. 
It is a Flask application that exposes an API endpoint for calculating delivery fees. 
The core function, calculate_delivery_fee, takes input parameters such as cart value, delivery distance, number of items, and delivery time, and returns the calculated delivery fee.

### `test.py`

The test file contains unit tests for the calculate_delivery_fee function and friday_rush_hour. 
The tests cover various scenarios, including edge cases, to ensure the correctness of the delivery fee calculation logic. 
The tests use the unittest framework.

## How to Run

`/calculate_delivery_fee` `(POST)`
This endpoint accepts a JSON payload with the following parameters:

- cart_value: The total value of items in the cart.
- delivery_distance: The distance of the delivery location.
- number_of_items: The total number of items in the cart.
- time: The timestamp of the delivery request in the format 'YYYY-MM-DDTHH:MM:SSZ'.

The endpoint returns a JSON response with the calculated delivery_fee.

### Example Request Using CURL:

> curl -X POST "http://localhost:5000/calculate_delivery_fee" -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}'

### Example Response:

> {"delivery_fee": 710}

## Running Tests

Execute the test.py file to run the unit tests. 
The tests validate the functionality of the calculate_delivery_fee function under different scenarios.

## Dependencies

- Flask
- unittest
