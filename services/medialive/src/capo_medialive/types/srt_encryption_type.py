"""Generated from Smithy shape ``com.amazonaws.medialive#SrtEncryptionType``."""

from typing import Literal, TypeAlias, cast

"""Srt Encryption Type"""
SrtEncryptionType: TypeAlias = Literal[
    "AES128",
    "AES192",
    "AES256",
]


# --- restJson1 ser/de ---
def serialize_json(value: SrtEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> SrtEncryptionType:
    return cast(SrtEncryptionType, data)
