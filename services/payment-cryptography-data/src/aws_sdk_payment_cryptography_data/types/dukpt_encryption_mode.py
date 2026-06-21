"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptEncryptionMode``."""

from typing import Literal, TypeAlias, cast

DukptEncryptionMode: TypeAlias = Literal[
    "ECB",
    "CBC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DukptEncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> DukptEncryptionMode:
    return cast(DukptEncryptionMode, data)
