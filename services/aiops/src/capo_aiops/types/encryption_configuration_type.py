"""Generated from Smithy shape ``com.amazonaws.aiops#EncryptionConfigurationType``."""

from typing import Literal, TypeAlias, cast

EncryptionConfigurationType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionConfigurationType:
    return cast(EncryptionConfigurationType, data)
