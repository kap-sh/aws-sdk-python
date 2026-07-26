"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ThumbnailStorageType``."""

from typing import Literal, TypeAlias, cast

ThumbnailStorageType: TypeAlias = Literal[
    "SEQUENTIAL",
    "LATEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailStorageType) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailStorageType:
    return cast(ThumbnailStorageType, data)
