"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexAlertState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The possible states of a multiplex alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
MultiplexAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SET",
        "CLEARED",
    )
)


def serialize_json(value: MultiplexAlertState) -> str:
    return value


def deserialize_json(data: str) -> MultiplexAlertState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultiplexAlertState value: {data!r}")
    return cast(MultiplexAlertState, data)
