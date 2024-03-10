from datetime import date, datetime
from decimal import Decimal
from enum import IntEnum
from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Numeric, PrimaryKeyConstraint, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated


class Currency(IntEnum):
    RUPEE = 1
    EURO = 2


class ItemType(IntEnum):
    CREDIT = 1
    DEBIT = 2


str_20 = Annotated[str, 20]
str_200 = Annotated[str, 200]
num_20_5 = Annotated[Decimal, Numeric(20, 5)]


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Portfolio(db.Model):
    __tablename__ = "portfolios"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement="auto",
    )
    name: Mapped[str_20] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )
    holding_currency: Mapped[int] = mapped_column(
        nullable=False,
    )
    inception_date: Mapped[date] = mapped_column(
        nullable=False,
    )

    def __init__(
        self,
        name: str,
        currency: Currency,
        inception_date: date,
    ) -> None:
        self.name = name
        self.holding_currency = currency
        self.inception_date = inception_date
        super().__init__()


class Investment(db.Model):
    __tablename__ = "investments"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement="auto",
    )
    name: Mapped[str_200] = mapped_column(
        String(200),
        nullable=False,
    )
    portfolio: Mapped[int] = mapped_column(
        ForeignKey(
            "portfolios.id",
            ondelete="CASCADE",
        ),
    )

    def __init__(
        self,
        name: str,
        portfolio: Portfolio,
    ) -> None:
        self.name = name
        self.portfolio = portfolio.id
        super().__init__()


class Item(db.Model):
    __tablename__ = "items"
    __table_args__ = (
        PrimaryKeyConstraint(
            "created_at",
            "investment",
            "type",
        ),
    )
    amount: Mapped[num_20_5] = mapped_column(
        nullable=False,
    )
    type: Mapped[int] = mapped_column(
        nullable=False,
    )
    related_expenses: Mapped[num_20_5] = mapped_column(
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
    )
    investment: Mapped[int] = mapped_column(
        ForeignKey(
            "investments.id",
            ondelete="CASCADE",
        ),
    )

    def __init__(
        self,
        amount: float,
        type: ItemType,
        investment: Investment,
        created_at: datetime,
        related_expenses: Optional[float] = None,
    ) -> None:
        self.amount = amount
        self.created_at = created_at
        self.investment = investment.id
        self.type = type
        self.related_expenses = related_expenses
        super().__init__()


class CreditItem(Item):
    def __init__(
        self,
        amount: float,
        investment: Investment,
        related_expenses: Optional[float] = None,
        created_at: Optional[datetime] = datetime.now(),
    ):
        super().__init__(
            amount=amount,
            type=ItemType.CREDIT,
            investment=investment,
            related_expenses=related_expenses,
            created_at=created_at,
        )


class DebitItem(Item):
    def __init__(
        self,
        amount: float,
        investment: Investment,
        related_expenses: Optional[float] = None,
        created_at: Optional[datetime] = datetime.now(),
    ):
        super().__init__(
            amount=amount,
            type=ItemType.DEBIT,
            investment=investment,
            related_expenses=related_expenses,
            created_at=created_at,
        )
