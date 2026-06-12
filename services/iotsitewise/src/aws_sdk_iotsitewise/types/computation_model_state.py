"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ComputationModelState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: ComputationModelState) -> str:
    return value


def deserialize_json(data: str) -> ComputationModelState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputationModelState value: {data!r}")
    return cast(ComputationModelState, data)
