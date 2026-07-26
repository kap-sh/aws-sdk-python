"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamType``."""

from typing import Literal, TypeAlias, cast

MediaStreamType: TypeAlias = Literal[
    "MixedAudio",
    "IndividualAudio",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamType) -> str:
    return value


def deserialize_json(data: str) -> MediaStreamType:
    return cast(MediaStreamType, data)
