"""Generated from Smithy shape ``com.amazonaws.iot#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KMS_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
