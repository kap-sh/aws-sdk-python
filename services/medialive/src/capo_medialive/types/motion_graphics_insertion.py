"""Generated from Smithy shape ``com.amazonaws.medialive#MotionGraphicsInsertion``."""

from typing import Literal, TypeAlias, cast

"""Motion Graphics Insertion"""
MotionGraphicsInsertion: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MotionGraphicsInsertion) -> str:
    return value


def deserialize_json(data: str) -> MotionGraphicsInsertion:
    return cast(MotionGraphicsInsertion, data)
