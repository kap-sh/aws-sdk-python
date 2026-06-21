"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaUriType``."""

from typing import Literal, TypeAlias, cast

MediaUriType: TypeAlias = Literal[
    "RTSP_URI",
    "FILE_URI",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaUriType) -> str:
    return value


def deserialize_json(data: str) -> MediaUriType:
    return cast(MediaUriType, data)
