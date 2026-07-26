"""Generated from Smithy shape ``com.amazonaws.xray#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

EncryptionStatus: TypeAlias = Literal[
    "UPDATING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStatus:
    return cast(EncryptionStatus, data)
