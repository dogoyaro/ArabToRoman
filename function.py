roman_numerals_mapping = {
    1000: ['M'],
    100: ['C', 'D', 'M'],
    10: ['X', 'L', 'C'],
    1: ['I', 'V', 'X']
}


def value_converter(value, denominator):
    romans_at_denominator = roman_numerals_mapping[denominator]

    if denominator == 1000:
        return value * romans_at_denominator[0]

    if value == 4:
        # return denominator value for 4
        roman_value = ''.join(romans_at_denominator[:2])
        return roman_value
    if value == 9:
        # return denominator value for 9
        roman_value = ''.join(romans_at_denominator[0::2])
        return roman_value
    if value < 5:
        # return unit value * value
        roman_value = romans_at_denominator[0] * value
        return roman_value
    if value >= 5:
        # return denominator value for 5 + value_converter(value - 5, denominator/10)
        five_value = romans_at_denominator[1]
        roman_value = five_value + value_converter(value - 5, denominator)
        return roman_value


def arabic_to_roman_converter(number, denominator=1000):
    if denominator == 1:
        return value_converter(number, 1)
    else:
        quotient, remainder = divmod(number, denominator)
        quotient_in_roman = value_converter(quotient, denominator)
        remainder_in_roman = arabic_to_roman_converter(
            remainder, denominator/10)
        return quotient_in_roman + remainder_in_roman


def validate_argument(maybe_number):
    try:
        value = int(maybe_number)
        if value < 1 or value > 3999:
            raise ValueError()
        return (value, None)
    except ValueError:
        return (None, 'Invalid argument, value must be an Integer between 1 and 3999')


def collect_user_argument():
    number = raw_input(prompt_message)
    value, error = validate_argument(number)
    if error:
        print(error)
        collect_user_argument()
    else:
        return value


if __name__ == '__main__':
    prompt_message = "Enter a number, e.g 1, 10, 222: "
    rerun_message = "Convert another number? (Y/n): "
    playing = True

    while playing:
        number = collect_user_argument()
        print(arabic_to_roman_converter(number))
        rerun = raw_input(rerun_message)
        if rerun.lower() != 'y':
            playing = False