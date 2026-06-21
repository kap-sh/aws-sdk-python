"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveChannelPipelineId``."""

from typing import Literal, TypeAlias, cast

MediaLiveChannelPipelineId: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveChannelPipelineId) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveChannelPipelineId:
    return cast(MediaLiveChannelPipelineId, data)
