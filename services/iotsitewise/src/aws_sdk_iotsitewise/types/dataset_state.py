"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

DatasetState: TypeAlias = Literal[
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


def serialize_json(value: DatasetState) -> str:
    return value


def deserialize_json(data: str) -> DatasetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetState value: {data!r}")
    return cast(DatasetState, data)
