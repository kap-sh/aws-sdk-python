"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EncryptionType``."""

from typing import Literal, TypeAlias, cast

EncryptionType: TypeAlias = Literal[
    "MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION",
    "CUSTOMER_KEY_ENCRYPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    return cast(EncryptionType, data)
