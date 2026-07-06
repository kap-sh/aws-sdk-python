"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaPinVerification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.integer_range_between0_and6
    import aws_sdk_payment_cryptography_data.types.verification_value_type


class VisaPinVerification(TypedDict, closed=True):
    pin_verification_key_index: "aws_sdk_payment_cryptography_data.types.integer_range_between0_and6.IntegerRangeBetween0And6"
    """<p>The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).</p>"""
    verification_value: "aws_sdk_payment_cryptography_data.types.verification_value_type.VerificationValueType"
    """<p>Parameters that are required to generate or verify Visa PVV (PIN Verification Value).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaPinVerification) -> dict:
    out: dict = {}
    out["PinVerificationKeyIndex"] = value["pin_verification_key_index"]
    out["VerificationValue"] = value["verification_value"]
    return out


def deserialize_json(data: dict) -> VisaPinVerification:
    out: VisaPinVerification = {}  # type: ignore[typeddict-item]
    if "PinVerificationKeyIndex" in data:
        out["pin_verification_key_index"] = data["PinVerificationKeyIndex"]
    else:
        raise DeserializationError(
            "VisaPinVerification.pin_verification_key_index required"
        )
    if "VerificationValue" in data:
        out["verification_value"] = data["VerificationValue"]
    else:
        raise DeserializationError("VisaPinVerification.verification_value required")
    return out
