"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptionConflictResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

EncryptionConflictResolutionStrategy: TypeAlias = Literal[
    "ALLOW",
    "SKIP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "SKIP",
    )
)


def serialize_json(value: EncryptionConflictResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptionConflictResolutionStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EncryptionConflictResolutionStrategy value: {data!r}"
        )
    return cast(EncryptionConflictResolutionStrategy, data)
