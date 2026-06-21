"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvEncryptionMode``."""

from typing import Literal, TypeAlias, cast

EmvEncryptionMode: TypeAlias = Literal[
    "ECB",
    "CBC",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmvEncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EmvEncryptionMode:
    return cast(EmvEncryptionMode, data)
