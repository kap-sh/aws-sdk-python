"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ActiveSpeakerPosition``."""

from typing import Literal, TypeAlias, cast

ActiveSpeakerPosition: TypeAlias = Literal[
    "TopLeft",
    "TopRight",
    "BottomLeft",
    "BottomRight",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveSpeakerPosition) -> str:
    return value


def deserialize_json(data: str) -> ActiveSpeakerPosition:
    return cast(ActiveSpeakerPosition, data)
