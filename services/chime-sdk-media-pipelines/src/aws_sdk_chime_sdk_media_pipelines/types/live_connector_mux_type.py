"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorMuxType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

LiveConnectorMuxType: TypeAlias = Literal[
    "AudioWithCompositedVideo",
    "AudioWithActiveSpeakerVideo",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AudioWithCompositedVideo",
        "AudioWithActiveSpeakerVideo",
    )
)


def serialize_json(value: LiveConnectorMuxType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorMuxType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LiveConnectorMuxType value: {data!r}")
    return cast(LiveConnectorMuxType, data)
