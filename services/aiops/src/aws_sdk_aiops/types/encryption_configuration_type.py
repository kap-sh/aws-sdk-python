"""Generated from Smithy shape ``com.amazonaws.aiops#EncryptionConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_aiops.errors import DeserializationError

EncryptionConfigurationType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KEY",
        "CUSTOMER_MANAGED_KMS_KEY",
    )
)


def serialize_json(value: EncryptionConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EncryptionConfigurationType value: {data!r}"
        )
    return cast(EncryptionConfigurationType, data)
