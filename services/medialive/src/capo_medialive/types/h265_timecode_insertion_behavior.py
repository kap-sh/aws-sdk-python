"""Generated from Smithy shape ``com.amazonaws.medialive#H265TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

"""H265 Timecode Insertion Behavior"""
H265TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "PIC_TIMING_SEI",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> H265TimecodeInsertionBehavior:
    return cast(H265TimecodeInsertionBehavior, data)
