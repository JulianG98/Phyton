# Jede Änderung an der Excel soll natürlich gespeichert werden!
# Drei Verkäufer: Markus, Jürgen und Jasmin
# Zwei Status/Stages: Offen (Cold Call), Abgeschlossen (Verkauf, Follow Up)
import openpyxl
from openpyxl.chart import Reference, Series
# Schreibe eine Funktion die neuen Kunde mit allen Wert ins CRM aufnimmt. Werte sollen über den Argparse hinzugefügt werden können. Und füge min. 10 Kunden mit verschiedenen Werten über diesen Aufruf hinzu in die Excel. 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-N", "--Name", dest="crm.xlsx", help="wie lautet der Name von dem Kunden", required=True)
parser.add_argument("-E", "--Email", dest="crm.xlsx", help="wie lauftet die email von dem Kunden", required=True)
parser.add_argument("-S", "--Status", dest="crm.xlsx", help="ist der verkauf abgeschlossen oder nicht", required=True)
parser.add_argument("-Sg", "--Stage", dest="crm.xlsx", help="in welcher Phase befinden wir uns", required=True)
parser.add_argument("-W", "--Wählversuche", dest="crm.xlsx", help="wie oft hat der verkäufer die Nummer gewählt", required=True)
parser.add_argument("-P", "--Produktverkaufspreis", dest="crm.xlsx", help="für wie viel wurde das Produkt verkauft", required=True)
parser.add_argument("-Z", "--Zeit bis Sale", dest="crm.xlsx", help="Wie viele Tage bis zum verkauf", required=True)
parser.add_argument("-V", "--Verkäufer", dest="crm.xlsx", help="Welcher Verkäufer hat den verkauf abgeschlossen", required=True)

args = parser.parse_args()
f = open(args.crm.xlsx, "r")
print("Alles: " + f.read())

wb= openpyxl.load_workbook("crm.xlsx", data_only= True)
Worksheet = wb.active
Worksheet["A5"] = "Raja König"
# Schreibe eine Funktion die bestehende Kundeneinträge im CRM aktualisiert. Werte sollen über den Argparse hinzugefügt werden können


# Schreibe eine Funktion die alle Kunden im Status "Offen" in ein neues Tabellenblatt "Offene Kunden" einfügt


# Schreibe eine Funktion die alle Kunden im Status "Abgeschlossen" in ein neues Tabellenblatt "Abgeschlossene Kunden" einfügt


# Schreibe eine Funktion die im Tabellenblatt "Abgeschlossene Kunden" den Gesamtverkaufpreis als Summe unten anfügt.


# Schreibe eine Funktion die im Tabellenblatt "Abgeschlossene Kunden" die durchschnittliche Zeit "Zeit bis zum Sale (Tage)" unten anfügt.


# Schreibe eine Funktion die im Tabellenblatt "Offene Kunde" ein BarChart hinzufügt welches auf der X-Achse die Namen der Verkäufer enthält und auf der Y-Achse deren Summe an Wählversuchen. Keine Duplikate!
# Das Chart sollte so aussehen:
#
#
#                                       
#                   |                   
#                   |                   |                   |
#                   |                   |                   | 
#                   |                   |                   |  
#               Verkäufer A         Verkäufer B         Verkäufer ..


# Schreibe eine Funktion die im Tabellenblatt "Abgeschlossene Kunden" ein BarChart hinzufügt welches auf der X-Achse die Namen der Verkäufer enthält und auf der Y-Achse deren Summe an Verkaufspreisen und deren durchschnittliche Zeit bis zum Sale anzeigt. Keine Duplikate!
# Das Chart sollte so aussehen:
#
#
#                                       |
#                   |                   |
#                   |                   |                   |
#                   |                   |                   | |
#                   | |                 | |                 | |  
#               Verkäufer A         Verkäufer B         Verkäufer ..