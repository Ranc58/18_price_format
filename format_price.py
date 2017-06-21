import argparse
import locale


def format_price(input_price):
    locale.setlocale(locale.LC_ALL, '')
    try:
        if isinstance(input_price, (int, float)):
            output_price = ("{:n}".format(round(input_price,2)))
        else:
            input_price = float(input_price.replace(',', '.'))
            output_price = "{:n}".format(round(input_price,2))
    except ValueError:
        return None
    else:
        return output_price.replace(u'\xa0', u' ')


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price',
                        help="set price")
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    options = create_parser_for_user_arguments()
    input_price = options.price
    output_price = format_price(input_price)
    if output_price is not None:
        print(output_price)
    else:
        print("Error! '{}'-incorrect value!".format(input_price))
