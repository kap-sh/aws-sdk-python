"""Generated from Smithy shape ``com.amazonaws.medialive#InputState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Placeholder documentation for InputState"""
InputState: TypeAlias = Literal[
    "CREATING",
    "DETACHED",
    "ATTACHED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DETACHED",
        "ATTACHED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: InputState) -> str:
    return value


def deserialize_json(data: str) -> InputState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputState value: {data!r}")
    return cast(InputState, data)
