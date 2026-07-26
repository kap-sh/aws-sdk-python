"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineSourceType``."""

from typing import Literal, TypeAlias, cast

MediaPipelineSourceType: TypeAlias = Literal["ChimeSdkMeeting",]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineSourceType) -> str:
    return value


def deserialize_json(data: str) -> MediaPipelineSourceType:
    return cast(MediaPipelineSourceType, data)
