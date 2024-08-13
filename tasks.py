import dotenv
import os

from robocorp.tasks import task
from RPA.Email.ImapSmtp import ImapSmtp
from RPA.Excel.Files import Files

dotenv.load_dotenv()

gmail_account = os.getenv("ACCOUNT_NAME")
app_password = os.getenv("APP_PASSWORD")
recepient = os.getenv("RECEPIENT")


@task
def mailing_with_exel_data():
    """Collects data from an Excel file and sends Emails with it"""
    emails = collect_data_and_create_emails()

    mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)
    mail.authorize(account=gmail_account, password=app_password)

    for email in emails:
        mail.send_message(
            sender=gmail_account,
            recipients=recepient,
            subject=email["email_header"],
            body=email["email_body"]
            )


def collect_data_and_create_emails():
    """Collects data from Excel file and creates a list of Emails"""
    excel = Files()
    excel.open_workbook("Beispielmappe1.xlsx")
    worksheet = excel.read_worksheet_as_table("Tabelle1", header=True)
    excel.close_workbook
    emails = []
    for row in worksheet:
        email_dict = dict(zip(['email_header', 'email_body'], construct_email(row)))
        emails.append(email_dict)
    return emails


def construct_email(data):
    """Constructs Email header and body with input data"""
    amount = data["Betrag"]
    doc_id = data["Aktzeichen"]
    first_name = data["Vorname"]
    index = data["PLZ"]
    last_name = data["Nachname"]
    region = data["Ort"]
    street = data["Straße"]
    
    # Creates full country name from country code
    country_code = data["Land"]
    country_dict = {
        "AT": "Österreich",
        "CH": "die Schweiz",
        #  TODO add more if necessary
        }
    country = country_dict[country_code] if country_code in country_dict.keys() else country_code
    
    # Creates greeting
    sex = data["Geschlecht"]
    greeting = "Sehr geehrter Herr" if sex == "M" else "Sehr geehrte Frau" if sex == "W" else "Sehr geehrte*r"
    
    header = f"Betreff: Bzgl. {doc_id}"
    body = f"""
    {greeting} {first_name} {last_name},
    Mit diesem Schreiben wollen wir Ihnen mitteilen, dass sie sich für eine Gutschrift im Wert von {amount}
    qualifizieren.
    Der Betrag wird automatisch auf den Vertrag {doc_id} mit der Adresse {street}, {index}, {region}, {country} gutgeschrieben.

    Mit freundlichen Grüßen,
    Max Mustermann
    """
    return header, body
