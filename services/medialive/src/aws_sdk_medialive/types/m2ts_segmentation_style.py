"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsSegmentationStyle``."""

from typing import Literal, TypeAlias, cast

"""M2ts Segmentation Style"""
M2tsSegmentationStyle: TypeAlias = Literal[
    "MAINTAIN_CADENCE",
    "RESET_CADENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSegmentationStyle) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationStyle:
    return cast(M2tsSegmentationStyle, data)
