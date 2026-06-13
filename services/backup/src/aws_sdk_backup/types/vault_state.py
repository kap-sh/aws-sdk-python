"""Generated from Smithy shape ``com.amazonaws.backup#VaultState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

VaultState: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "FAILED",
    )
)


def serialize_json(value: VaultState) -> str:
    return value


def deserialize_json(data: str) -> VaultState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VaultState value: {data!r}")
    return cast(VaultState, data)
