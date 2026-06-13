"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dsql.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
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


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
