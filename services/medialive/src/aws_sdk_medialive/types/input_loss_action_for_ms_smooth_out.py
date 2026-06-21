"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForMsSmoothOut``."""

from typing import Literal, TypeAlias, cast

"""Input Loss Action For Ms Smooth Out"""
InputLossActionForMsSmoothOut: TypeAlias = Literal[
    "EMIT_OUTPUT",
    "PAUSE_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputLossActionForMsSmoothOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForMsSmoothOut:
    return cast(InputLossActionForMsSmoothOut, data)
