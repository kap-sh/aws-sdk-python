"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveInputPipelineId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

MediaLiveInputPipelineId: TypeAlias = Literal[
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


def serialize_json(value: MediaLiveInputPipelineId) -> str:
    return value


def deserialize_json(data: str) -> MediaLiveInputPipelineId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaLiveInputPipelineId value: {data!r}")
    return cast(MediaLiveInputPipelineId, data)
