"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanStatus``."""

from typing import Literal, TypeAlias, cast

ImageScanStatus: TypeAlias = Literal[
    "PENDING",
    "SCANNING",
    "COLLECTING",
    "COMPLETED",
    "ABANDONED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageScanStatus:
    return cast(ImageScanStatus, data)
