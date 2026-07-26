"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveInputPipelineId``."""

from typing import Literal, TypeAlias, cast

MediaLiveInputPipelineId: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveInputPipelineId) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveInputPipelineId:
    return cast(MediaLiveInputPipelineId, data)
