def main():
    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?


def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    # If we have no prices, return 0 as in no discount.
    if len(item_prices) == 0:
        return 0

    # If our array is 3 entries or more, get lowest value in item price array and return it.
    if len(item_prices) >= 3:
        return min(item_prices)

    # Any other case, we return 0 or no discount.
    return 0


if __name__ == '__main__':
    main()