from sqlalchemy import Column, BigInteger, Integer, Text, Date, Numeric, Boolean, DOUBLE_PRECISION
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Models:
    class Users(Base):
        __tablename__ = 'users'
        id_user = Column(BigInteger)
        name = Column(Text)
        lastname = Column(Text)
        username = Column(Text)
        is_user = Column(Boolean)
        date = Column(Date)
        lang_code = Column(Text)

    class RefSystem(Base):
        __tablename__ = 'ref_system'
        id_user = Column(BigInteger)
        id_ref = Column(BigInteger)


    class BanSystem(Base):
        __tablename__ = 'ban_system'
        id_user = Column(BigInteger)
        info = Column(Text)
        date = Column(Date)


    class CryptoBalance(Base):
        __tablename__ = 'crypto_balance'
        id_user = Column(BigInteger)
        crypto = Column(Text)
        count = Column(Numeric)


    class CurrencyBalance(Base):
        __tablename__ = 'currency_balance'
        id_user = Column(BigInteger)
        currency = Column(Text)
        count = Column(Numeric)

    class Topup(Base):
        __tablename__ = 'topup'

