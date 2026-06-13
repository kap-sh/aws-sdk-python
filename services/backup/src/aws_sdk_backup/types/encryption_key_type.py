"""Generated from Smithy shape ``com.amazonaws.backup#EncryptionKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

EncryptionKeyType: TypeAlias = Literal[
    "AWS_OWNED_KMS_KEY",
    "CUSTOMER_MANAGED_KMS_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KMS_KEY",
        "CUSTOMER_MANAGED_KMS_KEY",
    )
)


def serialize_json(value: EncryptionKeyType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionKeyType value: {data!r}")
    return cast(EncryptionKeyType, data)
