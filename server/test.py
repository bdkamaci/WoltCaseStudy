import unittest
import json
from datetime import datetime
from server.main import calculate_delivery_fee, app


class TestDeliveryFeeCalculation(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_calculate_delivery_fee(self):
        # Zero Case
        result = calculate_delivery_fee(10000, 0, 0, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 0, f"Expected 0, but got {result}")

        result = calculate_delivery_fee(0, 1000, 0, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 0, f"Expected 0, but got {result}")

        result = calculate_delivery_fee(0, 0, 3, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 0, f"Expected 0, but got {result}")

        # When cart value is less than 20000, delivery distance is less than 1000, and number of items is less than 5
        result = calculate_delivery_fee(10000, 500, 4, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 200, f"Expected 200, but got {result}")

        # When cart value is greater than or equal to 20000
        result = calculate_delivery_fee(20000, 500, 4, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 0, f"Expected 0, but got {result}")

        # When delivery distance is exactly 1000
        result = calculate_delivery_fee(10000, 1000, 4, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 200, f"Expected 200, but got {result}")

        # When number of items is exactly 5
        result = calculate_delivery_fee(10000, 500, 5, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 250, f"Expected 250, but got {result}")

        # When number of items is exactly 12
        result = calculate_delivery_fee(10000, 500, 12, '2024-01-01T12:00:00Z')
        self.assertEqual(round(result), 600, f"Expected 600, but got {result}")


    def test_calculate_delivery_fee_friday_rush_hour(self):
        # When time is within the rush hours
        result = calculate_delivery_fee(10000, 500, 4, '2022-01-01T18:00:00Z')
        self.assertEqual(round(result), 240, f"Expected 240, but got {result}")

        result = calculate_delivery_fee(790, 2235, 4, '2024-01-15T18:00:00Z')
        self.assertEqual(round(result), 852, f"Expected 100, but got {result}")

        # When time is not within the rush hours
        result = calculate_delivery_fee(10000, 500, 4, '2022-01-01T12:00:00Z')
        self.assertEqual(round(result), 200, f"Expected 200, but got {result}")

        result = calculate_delivery_fee(790, 2235, 4, '2024-01-15T13:00:00Z')
        self.assertEqual(round(result), 710, f"Expected 100, but got {result}")
