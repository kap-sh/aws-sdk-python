"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

EncryptionStrategy: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_OWNED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED",
        "AWS_OWNED",
    )
)


def serialize_json(value: EncryptionStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionStrategy value: {data!r}")
    return cast(EncryptionStrategy, data)
