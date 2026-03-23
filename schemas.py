from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal

class PaymentRequest(BaseModel):

    payment_id: str
    debtor_account: str
    creditor_account: str
    currency: str = Field(..., pattern="^(USD|CAD|EUR)$")
    amount: Decimal
    value_date: date
    payment_type: str = Field(..., pattern="^(DOMESTIC|NOSTRO_FUNDING)$")
    reference: str


class PaymentResponse(BaseModel):

    transaction_id: str
    status: str