"""Generated from Smithy shape ``com.amazonaws.medialive#SrtEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Srt Encryption Type"""
SrtEncryptionType: TypeAlias = Literal[
    "AES128",
    "AES192",
    "AES256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES128",
        "AES192",
        "AES256",
    )
)


def serialize_json(value: SrtEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> SrtEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SrtEncryptionType value: {data!r}")
    return cast(SrtEncryptionType, data)
