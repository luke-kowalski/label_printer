import pyodbc
import src.settings as settings
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import mm
import win32api
import win32print


GHOSTSCRIPT_PATH = settings.printer_GHOSTSCRIPT_PATH
GSPRINT_PATH = settings.printer_GSPRINT_PATH
currentprinter = win32print.GetDefaultPrinter()

conn_STRING = "DRIVER={};SERVER={};DATABASE={};UID={};PWD={}".format(
    settings.sql_driver,
    settings.sql_server,
    settings.sql_database,
    settings.sql_username,
    settings.sql_password,
)


def get_user_input():
    print("Podaj nazwę zlecenia: ")
    order_id = str(input())
    get_sql_data(order_id)


def get_sql_data(order_id):

    with open(settings.sql_query, "r", encoding="UTF-8") as f:
        data = f.read()
    try:
        with pyodbc.connect(conn_STRING) as conn:
            rows = conn.execute(data, (order_id)).fetchall()
    except pyodbc.Error as e:
        sqlstate = e.args[1]
        print(f"ERROR: {sqlstate}")
    else:
        render_pdf(rows)


def render_pdf(rows):

    path = settings.pdf_output_dir
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)
        print(f"Directory has been created: {path}")

    for row in rows:
        filename = path + row.NAME + ".pdf"

        canvas = Canvas(filename, pagesize=(100 * mm, 60 * mm))
        canvas.setFont("Times-Roman", 10)
        canvas.drawString(5 * mm, 50 * mm, f"{row.NAME} - {row.ID}")
        canvas.line(0 * mm, 49 * mm, 100 * mm, 49 * mm)
        canvas.save()

        win32api.ShellExecute(
            0,
            "open",
            GSPRINT_PATH,
            '-ghostscript "'
            + GHOSTSCRIPT_PATH
            + '" -printer "'
            + currentprinter
            + '" '
            + filename
            + "",
            ".",
            0,
        )