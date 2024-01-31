def main():
    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?


def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    # If we have two or lower prices, return 0 as in no discount.
    if len(item_prices) <= 2:
        return 0

    converted_array = []

    # iterate over our given array and check if something is a string
    # if it is a string, we try to convert, if it fails we don't add it to our new array
    for x in item_prices:
        if isinstance(x, str):
            converted_string = convertstring(x)
            if converted_string != -1:
                converted_array.append(converted_string)
        else:
            converted_array.append(x)

    return min(converted_array)


def convertstring(input_string):
    # If it is a digit, it is an int so convert and send back.
    if input_string.isdigit():
        return int(input_string)
    else:
        # try to convert to float
        # if we can, return the float, otherwise return back input.
        try:
            return float(input_string)
        except ValueError:
            # if we run into an error, we return -1 as a "could not convert" instead.
            return -1


if __name__ == '__main__':
    main()