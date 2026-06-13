"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KEY",
        "CUSTOMER_MANAGED_KEY",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
