"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptDerivationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

DukptDerivationType: TypeAlias = Literal[
    "TDES_2KEY",
    "TDES_3KEY",
    "AES_128",
    "AES_192",
    "AES_256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TDES_2KEY",
        "TDES_3KEY",
        "AES_128",
        "AES_192",
        "AES_256",
    )
)


def serialize_json(value: DukptDerivationType) -> str:
    return value


def deserialize_json(data: str) -> DukptDerivationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DukptDerivationType value: {data!r}")
    return cast(DukptDerivationType, data)
