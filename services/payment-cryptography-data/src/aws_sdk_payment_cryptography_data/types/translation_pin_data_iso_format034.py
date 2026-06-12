"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslationPinDataIsoFormat034``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class TranslationPinDataIsoFormat034(TypedDict):
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslationPinDataIsoFormat034) -> dict:
    out: dict = {}
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    return out


def deserialize_json(data: dict) -> TranslationPinDataIsoFormat034:
    out: TranslationPinDataIsoFormat034 = {}  # type: ignore[typeddict-item]
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "TranslationPinDataIsoFormat034.primary_account_number required"
        )
    return out
