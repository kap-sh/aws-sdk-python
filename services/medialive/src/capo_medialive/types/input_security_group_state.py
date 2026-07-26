"""Generated from Smithy shape ``com.amazonaws.medialive#InputSecurityGroupState``."""

from typing import Literal, TypeAlias, cast

"""Placeholder documentation for InputSecurityGroupState"""
InputSecurityGroupState: TypeAlias = Literal[
    "IDLE",
    "IN_USE",
    "UPDATING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSecurityGroupState) -> str:
    return value


def deserialize_json(data: str) -> InputSecurityGroupState:
    return cast(InputSecurityGroupState, data)
