"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamPipelineSinkType``."""

from typing import Literal, TypeAlias, cast

MediaStreamPipelineSinkType: TypeAlias = Literal["KinesisVideoStreamPool",]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamPipelineSinkType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamPipelineSinkType:
    return cast(MediaStreamPipelineSinkType, data)
