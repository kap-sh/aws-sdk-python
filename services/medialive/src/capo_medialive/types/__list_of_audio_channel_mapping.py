"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioChannelMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.audio_channel_mapping

__listOfAudioChannelMapping: TypeAlias = list[
    "capo_medialive.types.audio_channel_mapping.AudioChannelMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioChannelMapping) -> list:
    import capo_medialive.types.audio_channel_mapping

    out: list = []
    for item in value:
        out.append(capo_medialive.types.audio_channel_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioChannelMapping:
    import capo_medialive.types.audio_channel_mapping

    out: __listOfAudioChannelMapping = []
    for item in data:
        out.append(capo_medialive.types.audio_channel_mapping.deserialize_json(item))
    return out
