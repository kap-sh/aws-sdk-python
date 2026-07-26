"""Generated from Smithy shape ``com.amazonaws.databrew#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

EncryptionMode: TypeAlias = Literal[
    "SSE-KMS",
    "SSE-S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    return cast(EncryptionMode, data)
