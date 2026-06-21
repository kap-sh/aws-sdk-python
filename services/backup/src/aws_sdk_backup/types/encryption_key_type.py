"""Generated from Smithy shape ``com.amazonaws.backup#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

EncryptionKeyType: TypeAlias = Literal[
    "AWS_OWNED_KMS_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionKeyType:
    return cast(EncryptionKeyType, data)
