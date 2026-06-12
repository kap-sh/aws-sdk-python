"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting 'Disabled' in the web interface also disables encryption."""
HlsEncryptionType: TypeAlias = Literal[
    "AES128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES128",
        "SAMPLE_AES",
    )
)


def serialize_json(value: HlsEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> HlsEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsEncryptionType value: {data!r}")
    return cast(HlsEncryptionType, data)
