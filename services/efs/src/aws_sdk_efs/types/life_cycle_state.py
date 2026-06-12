"""Generated from Smithy shape ``com.amazonaws.efs#LifeCycleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

LifeCycleState: TypeAlias = Literal[
    "creating",
    "available",
    "updating",
    "deleting",
    "deleted",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creating",
        "available",
        "updating",
        "deleting",
        "deleted",
        "error",
    )
)


def serialize_json(value: LifeCycleState) -> str:
    return value


def deserialize_json(data: str) -> LifeCycleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifeCycleState value: {data!r}")
    return cast(LifeCycleState, data)
