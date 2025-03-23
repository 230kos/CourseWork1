import pandas as pd

from src.reports import spending_by_category
from src.services import simple_search
from src.views import main_page

if __name__ == "__main__":
    transactions = pd.read_excel("../data/operations.xlsx")
    print(main_page("2025-03-16 21:00:00"))
    print(simple_search("Перекрёсток", transactions.to_dict(orient="records")))
    print(spending_by_category(transactions, "Супермаркеты", "2021-10-19"))
