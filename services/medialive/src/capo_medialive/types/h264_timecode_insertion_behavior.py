"""Generated from Smithy shape ``com.amazonaws.medialive#H264TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

"""H264 Timecode Insertion Behavior"""
H264TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "PIC_TIMING_SEI",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> H264TimecodeInsertionBehavior:
    return cast(H264TimecodeInsertionBehavior, data)
