"""Generated from Smithy shape ``com.amazonaws.glacier#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
