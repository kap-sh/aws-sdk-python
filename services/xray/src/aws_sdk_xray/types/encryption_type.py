"""Generated from Smithy shape ``com.amazonaws.xray#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "NONE",
    "KMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "KMS",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
