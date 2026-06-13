"""Generated from Smithy shape ``com.amazonaws.supplychain#InstanceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

InstanceState: TypeAlias = Literal[
    "Initializing",
    "Active",
    "CreateFailed",
    "DeleteFailed",
    "Deleting",
    "Deleted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "Active",
        "CreateFailed",
        "DeleteFailed",
        "Deleting",
        "Deleted",
    )
)


def serialize_json(value: InstanceState) -> str:
    return value


def deserialize_json(data: str) -> InstanceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceState value: {data!r}")
    return cast(InstanceState, data)
