"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Timecode Insertion Behavior"""
Mpeg2TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "GOP_TIMECODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2TimecodeInsertionBehavior:
    return cast(Mpeg2TimecodeInsertionBehavior, data)
