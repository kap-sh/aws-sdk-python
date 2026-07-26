"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VideoMuxType``."""

from typing import Literal, TypeAlias, cast

VideoMuxType: TypeAlias = Literal["VideoOnly",]


# --- restJson1 ser/de ---
def serialize_json(value: VideoMuxType) -> str:
    return value


def deserialize_json(data: str) -> VideoMuxType:
    return cast(VideoMuxType, data)
