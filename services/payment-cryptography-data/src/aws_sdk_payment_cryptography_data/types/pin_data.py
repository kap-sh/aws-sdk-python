"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.pin_offset_type
    import aws_sdk_payment_cryptography_data.types.verification_value_type


class _PinData_PinOffset(TypedDict):
    PinOffset: "aws_sdk_payment_cryptography_data.types.pin_offset_type.PinOffsetType"


class _PinData_VerificationValue(TypedDict):
    VerificationValue: "aws_sdk_payment_cryptography_data.types.verification_value_type.VerificationValueType"


PinData: TypeAlias = _PinData_PinOffset | _PinData_VerificationValue


# --- restJson1 ser/de ---
def serialize_json(value: PinData) -> dict:
    if "PinOffset" in value:
        return {"PinOffset": value["PinOffset"]}
    elif "VerificationValue" in value:
        return {"VerificationValue": value["VerificationValue"]}
    else:
        raise SerializationError("PinData: no variant present")


def deserialize_json(data: dict) -> PinData:
    if "PinOffset" in data:
        return {"PinOffset": data["PinOffset"]}
    elif "VerificationValue" in data:
        return {"VerificationValue": data["VerificationValue"]}
    else:
        raise DeserializationError("PinData: no recognized variant key")
