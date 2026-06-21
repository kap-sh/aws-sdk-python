"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DecryptionMode``."""

from typing import Literal, TypeAlias, cast

"""Specify the encryption mode that you used to encrypt your input files."""
DecryptionMode: TypeAlias = Literal[
    "AES_CTR",
    "AES_CBC",
    "AES_GCM",
]


# --- restJson1 ser/de ---
def serialize_json(value: DecryptionMode) -> str:
    return value


def deserialize_json(data: str) -> DecryptionMode:
    return cast(DecryptionMode, data)
