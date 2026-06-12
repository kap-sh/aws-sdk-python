"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PaddingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_payment_cryptography_data.errors import DeserializationError

PaddingType: TypeAlias = Literal[
    "PKCS1",
    "OAEP_SHA1",
    "OAEP_SHA256",
    "OAEP_SHA512",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PKCS1",
        "OAEP_SHA1",
        "OAEP_SHA256",
        "OAEP_SHA512",
    )
)


def serialize_json(value: PaddingType) -> str:
    return value


def deserialize_json(data: str) -> PaddingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaddingType value: {data!r}")
    return cast(PaddingType, data)
