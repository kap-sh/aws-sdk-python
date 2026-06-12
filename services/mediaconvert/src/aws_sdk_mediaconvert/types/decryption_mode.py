"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DecryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the encryption mode that you used to encrypt your input files."""
DecryptionMode: TypeAlias = Literal[
    "AES_CTR",
    "AES_CBC",
    "AES_GCM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES_CTR",
        "AES_CBC",
        "AES_GCM",
    )
)


def serialize_json(value: DecryptionMode) -> str:
    return value


def deserialize_json(data: str) -> DecryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecryptionMode value: {data!r}")
    return cast(DecryptionMode, data)
