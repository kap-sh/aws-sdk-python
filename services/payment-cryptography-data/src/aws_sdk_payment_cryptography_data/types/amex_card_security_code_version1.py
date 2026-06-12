"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#AmexCardSecurityCodeVersion1``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.card_expiry_date_type


class AmexCardSecurityCodeVersion1(TypedDict):
    card_expiry_date: "aws_sdk_payment_cryptography_data.types.card_expiry_date_type.CardExpiryDateType"
    """<p>The expiry date of a payment card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmexCardSecurityCodeVersion1) -> dict:
    out: dict = {}
    out["CardExpiryDate"] = value["card_expiry_date"]
    return out


def deserialize_json(data: dict) -> AmexCardSecurityCodeVersion1:
    out: AmexCardSecurityCodeVersion1 = {}  # type: ignore[typeddict-item]
    if "CardExpiryDate" in data:
        out["card_expiry_date"] = data["CardExpiryDate"]
    else:
        raise DeserializationError(
            "AmexCardSecurityCodeVersion1.card_expiry_date required"
        )
    return out
