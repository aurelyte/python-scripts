def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return ('The price should be a number')
    elif not isinstance(discount, (int, float)):
        return ('The discount should be a number')
    elif price <= 0:
        return ('The price should be greater than 0')
    elif discount < 0 or discount > 100:
        return ('The discount should be between 0 and 100')
    else:
        return price * (1 - discount / 100)

"""
Tests:
Passed:1. You should have a function named apply_discount.
Passed:2. Your apply_discount function should take two parameters: price and discount.
Passed:3. When apply_discount is called with a price (first argument) that is not a number (int or float) it should return The price should be a number.
Passed:4. When apply_discount is called with a discount (second argument) that is not a number (int or float) it should return The discount should be a number.
Passed:5. When apply_discount is called with a price lower than or equal to 0, it should return The price should be greater than 0.
Passed:6. When apply_discount is called with a discount lower than 0 or greater than 100, it should return The discount should be between 0 and 100.
Passed:7. apply_discount(100, 20) should return 80.
Passed:8. apply_discount(200, 50) should return 100.
Passed:9. apply_discount(50, 0) should return 50.
Passed:10. When apply_discount is called with a discount of 100, it should return 0.
Passed:11. apply_discount(74.5, 20.0) should return 59.6.
"""
