"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaPin``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.integer_range_between0_and6


class VisaPin(TypedDict, closed=True):
    pin_verification_key_index: "aws_sdk_payment_cryptography_data.types.integer_range_between0_and6.IntegerRangeBetween0And6"
    """<p>The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaPin) -> dict:
    out: dict = {}
    out["PinVerificationKeyIndex"] = value["pin_verification_key_index"]
    return out


def deserialize_json(data: dict) -> VisaPin:
    out: VisaPin = {}  # type: ignore[typeddict-item]
    if "PinVerificationKeyIndex" in data:
        out["pin_verification_key_index"] = data["PinVerificationKeyIndex"]
    else:
        raise DeserializationError("VisaPin.pin_verification_key_index required")
    return out
