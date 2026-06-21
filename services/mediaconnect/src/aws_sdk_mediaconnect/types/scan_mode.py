"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ScanMode``."""

from typing import Literal, TypeAlias, cast

ScanMode: TypeAlias = Literal[
    "progressive",
    "interlace",
    "progressive-segmented-frame",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanMode) -> str:
    return value


def deserialize_json(data: str) -> ScanMode:
    return cast(ScanMode, data)
