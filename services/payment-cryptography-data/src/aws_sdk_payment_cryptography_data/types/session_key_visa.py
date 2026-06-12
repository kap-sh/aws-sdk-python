"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyVisa``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.number_length_equals2
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class SessionKeyVisa(TypedDict):
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: "aws_sdk_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyVisa) -> dict:
    out: dict = {}
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    return out


def deserialize_json(data: dict) -> SessionKeyVisa:
    out: SessionKeyVisa = {}  # type: ignore[typeddict-item]
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError("SessionKeyVisa.primary_account_number required")
    if "PanSequenceNumber" in data:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("SessionKeyVisa.pan_sequence_number required")
    return out
