import math
from datetime import datetime
import json
from flask import Flask, request

app = Flask(__name__)


def distances_surcharge(delivery_dist):
    if delivery_dist > 1000:
        return max(1, (math.ceil((delivery_dist - 1000) / 500))) * 100
    return 0


def items_surcharge(items):
    itm_surcharge = 0
    if items >= 5:
        itm_surcharge = 0.5 * (items - 4) * 100
        if items > 12:
            itm_surcharge += 120
    return itm_surcharge


def calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time):
    # TO DO: Get rid of the second part of the equation after validation is added
    if (cart_value >= 20000) or (not cart_value or not delivery_distance or not number_of_items):
        return 0

    # TO DO: Read static values from environment variable or from a constant that define it.
    time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
    friday_rush_start_time = time.replace(hour=15, minute=0, second=0)
    friday_rush_end_time = time.replace(hour=19, minute=0, second=0)

    small_order_surcharge = 0 if cart_value > 1000 else (1000 - cart_value)
    base_delivery_fee = 200

    distance_surcharge = distances_surcharge(delivery_distance)
    item_surcharge = items_surcharge(number_of_items)

    is_friday_rush = 1 if (friday_rush_start_time <= time) & (time <= friday_rush_end_time) else 0

    rush_multiplier = 1.2 if is_friday_rush else 1

    total_fee_before_rush = base_delivery_fee + distance_surcharge + item_surcharge + small_order_surcharge

    fee = total_fee_before_rush * rush_multiplier

    delivery_fee = min(fee, 1500)

    return delivery_fee


@app.route('/calculate_delivery_fee', methods=['POST'])
def calculate_delivery_fee_route():
    data = request.get_json()

    # TO DO: Add validation function and related test.
    # TO DO: Throw 400 Bad Request Error if faced a validation error.
    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance']
    number_of_items = data['number_of_items']
    time = data['time']

    delivery_fee = calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time)

    response_payload = {'delivery_fee': delivery_fee}

    return json.dumps(response_payload), 200


if __name__ == '__main__':
    app.run(debug=True)
