"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivationValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.application_cryptogram_type
    import aws_sdk_payment_cryptography_data.types.hex_length_equals4


class _SessionKeyDerivationValue_ApplicationCryptogram(TypedDict):
    ApplicationCryptogram: "aws_sdk_payment_cryptography_data.types.application_cryptogram_type.ApplicationCryptogramType"


class _SessionKeyDerivationValue_ApplicationTransactionCounter(TypedDict):
    ApplicationTransactionCounter: (
        "aws_sdk_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )


SessionKeyDerivationValue: TypeAlias = (
    _SessionKeyDerivationValue_ApplicationCryptogram
    | _SessionKeyDerivationValue_ApplicationTransactionCounter
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyDerivationValue) -> dict:
    if "ApplicationCryptogram" in value:
        return {"ApplicationCryptogram": value["ApplicationCryptogram"]}
    elif "ApplicationTransactionCounter" in value:
        return {"ApplicationTransactionCounter": value["ApplicationTransactionCounter"]}
    else:
        raise SerializationError("SessionKeyDerivationValue: no variant present")


def deserialize_json(data: dict) -> SessionKeyDerivationValue:
    if "ApplicationCryptogram" in data:
        return {"ApplicationCryptogram": data["ApplicationCryptogram"]}
    elif "ApplicationTransactionCounter" in data:
        return {"ApplicationTransactionCounter": data["ApplicationTransactionCounter"]}
    else:
        raise DeserializationError(
            "SessionKeyDerivationValue: no recognized variant key"
        )
