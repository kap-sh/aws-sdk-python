"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

EncryptionMode: TypeAlias = Literal[
    "ECB",
    "CBC",
    "CFB",
    "CFB1",
    "CFB8",
    "CFB64",
    "CFB128",
    "OFB",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    return cast(EncryptionMode, data)
