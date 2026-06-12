"""Generated from Smithy shape ``com.amazonaws.mediapackage#EncryptionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

EncryptionMethod: TypeAlias = Literal[
    "AES_128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES_128",
        "SAMPLE_AES",
    )
)


def serialize_json(value: EncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionMethod value: {data!r}")
    return cast(EncryptionMethod, data)
