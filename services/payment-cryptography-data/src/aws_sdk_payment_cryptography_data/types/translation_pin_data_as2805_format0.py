"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslationPinDataAs2805Format0``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.primary_account_number_type


class TranslationPinDataAs2805Format0(TypedDict, closed=True):
    primary_account_number: "aws_sdk_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslationPinDataAs2805Format0) -> dict:
    out: dict = {}
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    return out


def deserialize_json(data: dict) -> TranslationPinDataAs2805Format0:
    out: TranslationPinDataAs2805Format0 = {}  # type: ignore[typeddict-item]
    if "PrimaryAccountNumber" in data:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "TranslationPinDataAs2805Format0.primary_account_number required"
        )
    return out
