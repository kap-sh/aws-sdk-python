"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailState``."""

from typing import Literal, TypeAlias, cast

"""Thumbnail State"""
ThumbnailState: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailState) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailState:
    return cast(ThumbnailState, data)
