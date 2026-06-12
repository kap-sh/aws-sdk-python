"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#As2805PekDerivationAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.system_trace_audit_number_type
    import aws_sdk_payment_cryptography_data.types.transaction_amount_type


class As2805PekDerivationAttributes(TypedDict):
    system_trace_audit_number: "aws_sdk_payment_cryptography_data.types.system_trace_audit_number_type.SystemTraceAuditNumberType"
    """<p>The system trace audit number for the transaction.</p>"""
    transaction_amount: "aws_sdk_payment_cryptography_data.types.transaction_amount_type.TransactionAmountType"
    """<p>The transaction amount for the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: As2805PekDerivationAttributes) -> dict:
    out: dict = {}
    out["SystemTraceAuditNumber"] = value["system_trace_audit_number"]
    out["TransactionAmount"] = value["transaction_amount"]
    return out


def deserialize_json(data: dict) -> As2805PekDerivationAttributes:
    out: As2805PekDerivationAttributes = {}  # type: ignore[typeddict-item]
    if "SystemTraceAuditNumber" in data:
        out["system_trace_audit_number"] = data["SystemTraceAuditNumber"]
    else:
        raise DeserializationError(
            "As2805PekDerivationAttributes.system_trace_audit_number required"
        )
    if "TransactionAmount" in data:
        out["transaction_amount"] = data["TransactionAmount"]
    else:
        raise DeserializationError(
            "As2805PekDerivationAttributes.transaction_amount required"
        )
    return out
