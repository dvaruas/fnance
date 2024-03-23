from typing import List

from fapp import db
from fapp.models import CreditItem, Currency, DebitItem, Investment, Portfolio


def portfolios() -> List[Portfolio]:
    return Portfolio.query.all()


def create_portfolio(p: Portfolio) -> None:
    db.session.add(p)
    db.session.commit()
