"""Generated from Smithy shape ``com.amazonaws.iot#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KMS_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED_KMS_KEY",
        "AWS_OWNED_KMS_KEY",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
