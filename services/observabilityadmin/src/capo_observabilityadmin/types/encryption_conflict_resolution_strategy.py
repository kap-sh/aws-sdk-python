"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptionConflictResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

EncryptionConflictResolutionStrategy: TypeAlias = Literal[
    "ALLOW",
    "SKIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConflictResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> EncryptionConflictResolutionStrategy:
    return cast(EncryptionConflictResolutionStrategy, data)
