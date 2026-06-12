"""Generated from Smithy shape ``com.amazonaws.synthetics#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

EncryptionMode: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSE_S3",
        "SSE_KMS",
    )
)


def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionMode value: {data!r}")
    return cast(EncryptionMode, data)
