"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

DukptEncryptionMode: TypeAlias = Literal[
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


def serialize_json(value: DukptEncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> DukptEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DukptEncryptionMode value: {data!r}")
    return cast(DukptEncryptionMode, data)
