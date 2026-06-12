"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The current state of the multiplex."""
MultiplexState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "IDLE",
    "STARTING",
    "RUNNING",
    "RECOVERING",
    "STOPPING",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "IDLE",
        "STARTING",
        "RUNNING",
        "RECOVERING",
        "STOPPING",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: MultiplexState) -> str:
    return value


def deserialize_json(data: str) -> MultiplexState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultiplexState value: {data!r}")
    return cast(MultiplexState, data)
