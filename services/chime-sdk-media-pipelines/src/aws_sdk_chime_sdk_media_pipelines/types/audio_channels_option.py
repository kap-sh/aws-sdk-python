"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioChannelsOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

AudioChannelsOption: TypeAlias = Literal[
    "Stereo",
    "Mono",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Stereo",
        "Mono",
    )
)


def serialize_json(value: AudioChannelsOption) -> str:
    return value


def deserialize_json(data: str) -> AudioChannelsOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioChannelsOption value: {data!r}")
    return cast(AudioChannelsOption, data)
