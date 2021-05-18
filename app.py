from models.dier import Dier
from datetime import datetime
from db.datamanager_csv import DataManagerCSV

dm = DataManagerCSV("data/dieren", "data/asielen.csv")
dieren = dm.get_dieren()
for dier in dieren:
    print(dier.naam)

dier_met_id 