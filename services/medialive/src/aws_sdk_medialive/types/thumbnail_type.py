"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailType``."""

from typing import Literal, TypeAlias, cast

"""Thumbnail type."""
ThumbnailType: TypeAlias = Literal[
    "UNSPECIFIED",
    "CURRENT_ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailType) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailType:
    return cast(ThumbnailType, data)
