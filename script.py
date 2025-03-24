import pdfkit
import sys
import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

input_file = sys.argv[1]
output_file = sys.argv[2]


path_obj = Path(input_file).resolve()
print("Windows path:", path_obj)
file_url = path_obj.parent.as_uri() #get the directory of the html file for baseUrl
print("File URL:", file_url)




wkhtmltopdf_path = resource_path("bin/wkhtmltopdf.exe")
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

env = Environment(loader=FileSystemLoader('.'))  # current folder for jinja
template = env.get_template(input_file)
baseUrl=file_url+"/"

html = template.render(
    baseUrl=baseUrl,
    title="My Page",
    name="שי פטרנק",
    cond=True,
    cond2=False,
    items=["Apples", "שדג", "Cherries"]
)

if len(sys.argv) != 3:
    print("Usage: html_to_pdf.exe input.html output.pdf")
    sys.exit(1)


options = {
    'enable-local-file-access': None  
}


pdfkit.from_string(html, output_file, configuration=config,options=options)
print(f"Converted {input_file} to {output_file}")