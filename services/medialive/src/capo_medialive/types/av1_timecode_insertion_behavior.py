"""Generated from Smithy shape ``com.amazonaws.medialive#Av1TimecodeInsertionBehavior``."""

from typing import Literal, TypeAlias, cast

"""Av1 Timecode Insertion Behavior"""
Av1TimecodeInsertionBehavior: TypeAlias = Literal[
    "DISABLED",
    "METADATA_OBU",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1TimecodeInsertionBehavior) -> str:
    return value


def deserialize_json(data: str) -> Av1TimecodeInsertionBehavior:
    return cast(Av1TimecodeInsertionBehavior, data)
