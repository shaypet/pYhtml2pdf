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
if not os.path.isfile(input_file):
    print(f"❌ Error: Input file does not exist: {input_file}")
    sys.exit(1)

path_obj = Path(input_file).resolve()
print("Windows path:", path_obj)
file_url = path_obj.parent.as_uri() #get the directory of the html file for baseUrl
print("File directory URL:", file_url)

output_path = Path(output_file)
output_path.parent.mkdir(parents=True, exist_ok=True) #create out directory if not exists


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