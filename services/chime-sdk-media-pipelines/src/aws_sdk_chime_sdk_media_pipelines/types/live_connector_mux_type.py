"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorMuxType``."""

from typing import Literal, TypeAlias, cast

LiveConnectorMuxType: TypeAlias = Literal[
    "AudioWithCompositedVideo",
    "AudioWithActiveSpeakerVideo",
]


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorMuxType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorMuxType:
    return cast(LiveConnectorMuxType, data)
