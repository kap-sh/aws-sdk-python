"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CryptogramVerificationArpcMethod2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.hex_length_equals8
    import aws_sdk_payment_cryptography_data.types.proprietary_authentication_data_type


class CryptogramVerificationArpcMethod2(TypedDict):
    card_status_update: (
        "aws_sdk_payment_cryptography_data.types.hex_length_equals8.HexLengthEquals8"
    )
    """<p>The data indicating whether the issuer approves or declines an online transaction using an EMV chip card.</p>"""
    proprietary_authentication_data: NotRequired[
        "aws_sdk_payment_cryptography_data.types.proprietary_authentication_data_type.ProprietaryAuthenticationDataType"
    ]
    """<p>The proprietary authentication data used by issuer for communication during online transaction using an EMV chip card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptogramVerificationArpcMethod2) -> dict:
    out: dict = {}
    out["CardStatusUpdate"] = value["card_status_update"]
    if "proprietary_authentication_data" in value:
        out["ProprietaryAuthenticationData"] = value["proprietary_authentication_data"]
    return out


def deserialize_json(data: dict) -> CryptogramVerificationArpcMethod2:
    out: CryptogramVerificationArpcMethod2 = {}  # type: ignore[typeddict-item]
    if "CardStatusUpdate" in data:
        out["card_status_update"] = data["CardStatusUpdate"]
    else:
        raise DeserializationError(
            "CryptogramVerificationArpcMethod2.card_status_update required"
        )
    if "ProprietaryAuthenticationData" in data:
        out["proprietary_authentication_data"] = data["ProprietaryAuthenticationData"]
    return out
