"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupEventStopBehavior``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Event Stop Behavior"""
SmoothGroupEventStopBehavior: TypeAlias = Literal[
    "NONE",
    "SEND_EOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupEventStopBehavior) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupEventStopBehavior:
    return cast(SmoothGroupEventStopBehavior, data)
