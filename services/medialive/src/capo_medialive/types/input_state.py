"""Generated from Smithy shape ``com.amazonaws.medialive#InputState``."""

from typing import Literal, TypeAlias, cast

"""Placeholder documentation for InputState"""
InputState: TypeAlias = Literal[
    "CREATING",
    "DETACHED",
    "ATTACHED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputState) -> str:
    return value


def deserialize_json(data: str) -> InputState:
    return cast(InputState, data)
