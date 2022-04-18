from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.optionxform = str
parser.read("config.ini"
            )
def change_order_id_in_ini(id_name):
    parser.set("SQL", "SQL_ORDER_ID", id_name)
    with open("config.ini", "w") as configfile:
        parser.write(configfile)
