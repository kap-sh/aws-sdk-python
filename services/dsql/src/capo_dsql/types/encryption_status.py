"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

EncryptionStatus: TypeAlias = Literal[
    "ENABLED",
    "UPDATING",
    "KMS_KEY_INACCESSIBLE",
    "ENABLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStatus:
    return cast(EncryptionStatus, data)
