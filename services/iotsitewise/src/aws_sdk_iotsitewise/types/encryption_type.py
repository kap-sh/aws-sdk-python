"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "SITEWISE_DEFAULT_ENCRYPTION",
    "KMS_BASED_ENCRYPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
