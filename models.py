from sqlalchemy import Column, String, Numeric, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from database import Base

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    external_payment_id = Column(String, nullable=False)

    debtor_account = Column(String, nullable=False)

    creditor_account = Column(String, nullable=False)

    currency = Column(String, nullable=False)

    amount = Column(Numeric, nullable=False)

    payment_type = Column(String, nullable=False)

    status = Column(String, default="RECEIVED")

    created_at = Column(DateTime, server_default=func.now())

    #this field was added in a second iteration...
    reference = Column(String, nullable=False)

class TransactionEvent(Base):

    __tablename__ = "transaction_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    transaction_id = Column(UUID(as_uuid=True))

    event_type = Column(String)

    event_details = Column(Text)

    created_at = Column(DateTime, server_default=func.now())
