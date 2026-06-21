"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsEncryptionType``."""

from typing import Literal, TypeAlias, cast

"""Encrypts the segments with the given encryption scheme. Leave blank to disable. Selecting 'Disabled' in the web interface also disables encryption."""
HlsEncryptionType: TypeAlias = Literal[
    "AES128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> HlsEncryptionType:
    return cast(HlsEncryptionType, data)
