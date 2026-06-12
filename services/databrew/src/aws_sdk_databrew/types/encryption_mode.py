"""Generated from Smithy shape ``com.amazonaws.databrew#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

EncryptionMode: TypeAlias = Literal[
    "SSE-KMS",
    "SSE-S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSE-KMS",
        "SSE-S3",
    )
)


def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionMode value: {data!r}")
    return cast(EncryptionMode, data)
