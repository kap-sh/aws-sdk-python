"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

EmvEncryptionMode: TypeAlias = Literal[
    "ECB",
    "CBC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECB",
        "CBC",
    )
)


def serialize_json(value: EmvEncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EmvEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmvEncryptionMode value: {data!r}")
    return cast(EmvEncryptionMode, data)
