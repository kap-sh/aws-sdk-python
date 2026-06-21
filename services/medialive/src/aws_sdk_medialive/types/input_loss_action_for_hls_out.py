"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForHlsOut``."""

from typing import Literal, TypeAlias, cast

"""Input Loss Action For Hls Out"""
InputLossActionForHlsOut: TypeAlias = Literal[
    "EMIT_OUTPUT",
    "PAUSE_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputLossActionForHlsOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForHlsOut:
    return cast(InputLossActionForHlsOut, data)
