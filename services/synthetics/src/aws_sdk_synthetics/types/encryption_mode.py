"""Generated from Smithy shape ``com.amazonaws.synthetics#EncryptionMode``."""

from typing import Literal, TypeAlias, cast

EncryptionMode: TypeAlias = Literal[
    "SSE_S3",
    "SSE_KMS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMode) -> str:
    return value


def deserialize_json(data: str) -> EncryptionMode:
    return cast(EncryptionMode, data)
