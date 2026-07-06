"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CardVerificationValue1``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.card_expiry_date_type
    import aws_sdk_payment_cryptography_data.types.service_code_type


class CardVerificationValue1(TypedDict, closed=True):
    card_expiry_date: "aws_sdk_payment_cryptography_data.types.card_expiry_date_type.CardExpiryDateType"
    """<p>The expiry date of a payment card.</p>"""
    service_code: (
        "aws_sdk_payment_cryptography_data.types.service_code_type.ServiceCodeType"
    )
    """<p>The service code of the payment card. This is different from Card Security Code (CSC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CardVerificationValue1) -> dict:
    out: dict = {}
    out["CardExpiryDate"] = value["card_expiry_date"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> CardVerificationValue1:
    out: CardVerificationValue1 = {}  # type: ignore[typeddict-item]
    if "CardExpiryDate" in data:
        out["card_expiry_date"] = data["CardExpiryDate"]
    else:
        raise DeserializationError("CardVerificationValue1.card_expiry_date required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("CardVerificationValue1.service_code required")
    return out
