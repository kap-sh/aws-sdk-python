"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

EncryptionMode: TypeAlias = Literal[
    "ECB",
    "CBC",
    "CFB",
    "CFB1",
    "CFB8",
    "CFB64",
    "CFB128",
    "OFB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECB",
        "CBC",
        "CFB",
        "CFB1",
        "CFB8",
        "CFB64",
        "CFB128",
        "OFB",
    )
)


def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionMode value: {data!r}")
    return cast(EncryptionMode, data)
