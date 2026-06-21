"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossActionForRtmpOut``."""

from typing import Literal, TypeAlias, cast

"""Input Loss Action For Rtmp Out"""
InputLossActionForRtmpOut: TypeAlias = Literal[
    "EMIT_OUTPUT",
    "PAUSE_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputLossActionForRtmpOut) -> str:
    return value


def deserialize_json(data: str) -> InputLossActionForRtmpOut:
    return cast(InputLossActionForRtmpOut, data)
