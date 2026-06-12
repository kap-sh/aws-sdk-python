"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaStreamType: TypeAlias = Literal[
    "MixedAudio",
    "IndividualAudio",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MixedAudio",
        "IndividualAudio",
    )
)


def serialize_json(value: MediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaStreamType value: {data!r}")
    return cast(MediaStreamType, data)
