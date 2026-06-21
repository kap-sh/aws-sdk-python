"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ThumbnailRecordingMode``."""

from typing import Literal, TypeAlias, cast

ThumbnailRecordingMode: TypeAlias = Literal[
    "INTERVAL",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailRecordingMode) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailRecordingMode:
    return cast(ThumbnailRecordingMode, data)
