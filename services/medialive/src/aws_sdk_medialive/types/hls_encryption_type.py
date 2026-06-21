"""Generated from Smithy shape ``com.amazonaws.medialive#HlsEncryptionType``."""

from typing import Literal, TypeAlias, cast

"""Hls Encryption Type"""
HlsEncryptionType: TypeAlias = Literal[
    "AES128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> HlsEncryptionType:
    return cast(HlsEncryptionType, data)
