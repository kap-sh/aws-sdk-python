"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.audio_description

__listOfAudioDescription: TypeAlias = list[
    "capo_medialive.types.audio_description.AudioDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioDescription) -> list:
    import capo_medialive.types.audio_description

    out: list = []
    for item in value:
        out.append(capo_medialive.types.audio_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioDescription:
    import capo_medialive.types.audio_description

    out: __listOfAudioDescription = []
    for item in data:
        out.append(capo_medialive.types.audio_description.deserialize_json(item))
    return out
