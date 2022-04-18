from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.optionxform = str
parser.read("config.ini")

sql_driver = parser.get("SERVER_CONN", "DRIVER")
sql_server = parser.get("SERVER_CONN", "SERVER")
sql_database = parser.get("SERVER_CONN", "DATABASE")
sql_username = parser.get("SERVER_CONN", "USERNAME")
sql_password = parser.get("SERVER_CONN", "PASSWORD")
sql_query = parser.get("SQL", "SQL_QUERRY")
# DIR
html_output_dir = parser.get("DIR", "HTML_OUTPUT_DIR")


