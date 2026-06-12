"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

CanaryState: TypeAlias = Literal[
    "CREATING",
    "READY",
    "STARTING",
    "RUNNING",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "READY",
        "STARTING",
        "RUNNING",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "ERROR",
        "DELETING",
    )
)


def serialize_json(value: CanaryState) -> str:
    return value


def deserialize_json(data: str) -> CanaryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CanaryState value: {data!r}")
    return cast(CanaryState, data)
