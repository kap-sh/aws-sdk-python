"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
