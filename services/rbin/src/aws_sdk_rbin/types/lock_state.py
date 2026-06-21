"""Generated from Smithy shape ``com.amazonaws.rbin#LockState``."""

from typing import Literal, TypeAlias, cast

LockState: TypeAlias = Literal[
    "locked",
    "pending_unlock",
    "unlocked",
]


# --- restJson1 ser/de ---
def serialize_json(value: LockState) -> str:
    return value


def deserialize_json(data: str) -> LockState:
    return cast(LockState, data)
