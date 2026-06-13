"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveChannelPipelineId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MediaLiveChannelPipelineId: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PIPELINE_0",
        "PIPELINE_1",
    )
)


def serialize_json(value: MediaLiveChannelPipelineId) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveChannelPipelineId:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaLiveChannelPipelineId value: {data!r}"
        )
    return cast(MediaLiveChannelPipelineId, data)
