"""Generated from Smithy shape ``com.amazonaws.glacier#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws:kms",
        "AES256",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
