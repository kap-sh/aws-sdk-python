"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioChannelsOption``."""

from typing import Literal, TypeAlias, cast

AudioChannelsOption: TypeAlias = Literal[
    "Stereo",
    "Mono",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioChannelsOption) -> str:
    return value


def deserialize_json(data: str) -> AudioChannelsOption:
    return cast(AudioChannelsOption, data)
