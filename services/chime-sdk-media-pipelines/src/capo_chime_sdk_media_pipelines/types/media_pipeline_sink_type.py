"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineSinkType``."""

from typing import Literal, TypeAlias, cast

MediaPipelineSinkType: TypeAlias = Literal["S3Bucket",]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineSinkType) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineSinkType:
    return cast(MediaPipelineSinkType, data)
