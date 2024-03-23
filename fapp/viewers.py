from datetime import date

from flask import Blueprint, redirect, render_template, url_for

import fapp.controllers as controllers
from fapp import db
from fapp.models import CreditItem, Currency, DebitItem, Investment, Portfolio

app_mod = Blueprint("viewers", __name__)


@app_mod.route("/")
def test():
    # try:
    #     p = Portfolio(
    #         currency=Currency.EURO, name="abcd", inception_date=date(2020, 12, 1)
    #     )
    #     db.session.add(p)
    #     db.session.commit()

    #     i = Investment(portfolio=p, name="i1")
    #     db.session.add(i)
    #     db.session.commit()

    #     itd = DebitItem(amount=12.45, investment=i)
    #     itc = CreditItem(amount=45, investment=i)
    #     db.session.add_all([itd, itc])
    #     db.session.commit()
    # except:
    #     print("we failed to add db, but this is okay")
    #     pass

    return render_template("portfolios.html")
