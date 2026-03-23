from sqlalchemy.orm import Session
from models import Transaction, TransactionEvent

def create_payment(db: Session, payment):

    transaction = Transaction(
        external_payment_id=payment.payment_id,
        debtor_account=payment.debtor_account,
        creditor_account=payment.creditor_account,
        currency=payment.currency,
        amount=payment.amount,
        payment_type=payment.payment_type,
        status="RECEIVED",
        reference=payment.reference
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    event = TransactionEvent(
        transaction_id=transaction.id,
        event_type="PAYMENT_RECEIVED",
        event_details="Payment request accepted"
    )

    db.add(event)
    db.commit()

    return transaction