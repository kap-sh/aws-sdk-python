"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureIntervalUnit``."""

from typing import Literal, TypeAlias, cast

"""Frame Capture Interval Unit"""
FrameCaptureIntervalUnit: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureIntervalUnit) -> str:
    return value


def deserialize_json(data: str) -> FrameCaptureIntervalUnit:
    return cast(FrameCaptureIntervalUnit, data)
