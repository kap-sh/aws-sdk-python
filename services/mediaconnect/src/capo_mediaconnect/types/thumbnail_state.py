"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ThumbnailState``."""

from typing import Literal, TypeAlias, cast

ThumbnailState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailState) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailState:
    return cast(ThumbnailState, data)
