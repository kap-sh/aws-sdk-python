"""Generated from Smithy shape ``com.amazonaws.rbin#LockState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

LockState: TypeAlias = Literal[
    "locked",
    "pending_unlock",
    "unlocked",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "locked",
        "pending_unlock",
        "unlocked",
    )
)


def serialize_json(value: LockState) -> str:
    return value


def deserialize_json(data: str) -> LockState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LockState value: {data!r}")
    return cast(LockState, data)
