"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ExecutionState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: ExecutionState) -> str:
    return value


def deserialize_json(data: str) -> ExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionState value: {data!r}")
    return cast(ExecutionState, data)
