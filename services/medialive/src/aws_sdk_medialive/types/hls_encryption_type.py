"""Generated from Smithy shape ``com.amazonaws.medialive#HlsEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Encryption Type"""
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
