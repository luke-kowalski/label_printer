from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.optionxform = str
parser.read("src\config.ini")

# SQL
sql_driver = parser.get("SERVER_CONN", "DRIVER")
sql_server = parser.get("SERVER_CONN", "SERVER")
sql_database = parser.get("SERVER_CONN", "DATABASE")
sql_username = parser.get("SERVER_CONN", "USERNAME")
sql_password = parser.get("SERVER_CONN", "PASSWORD")
sql_query = parser.get("SQL", "SQL_QUERY_FILE_PATH")

# DIR
pdf_output_dir = parser.get("DIR", "PDF_OUTPUT_DIR")

# PRINTER
printer_GHOSTSCRIPT_PATH = parser.get("PRINTER", "GHOSTSCRIPT_PATH")
printer_GSPRINT_PATH = parser.get("PRINTER", "GSPRINT_PATH")