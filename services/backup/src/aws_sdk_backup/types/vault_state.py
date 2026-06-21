"""Generated from Smithy shape ``com.amazonaws.backup#VaultState``."""

from typing import Literal, TypeAlias, cast

VaultState: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VaultState) -> str:
    return value


def deserialize_json(data: str) -> VaultState:
    return cast(VaultState, data)
