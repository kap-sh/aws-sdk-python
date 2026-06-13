"""Generated from Smithy shape ``com.amazonaws.s3files#LifeCycleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3files.errors import DeserializationError

LifeCycleState: TypeAlias = Literal[
    "available",
    "creating",
    "deleting",
    "deleted",
    "error",
    "updating",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "creating",
        "deleting",
        "deleted",
        "error",
        "updating",
    )
)


def serialize_json(value: LifeCycleState) -> str:
    return value


def deserialize_json(data: str) -> LifeCycleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifeCycleState value: {data!r}")
    return cast(LifeCycleState, data)
