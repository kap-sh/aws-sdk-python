"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfAudioChannelTag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.audio_channel_tag

__listOfAudioChannelTag: TypeAlias = list[
    "capo_mediaconvert.types.audio_channel_tag.AudioChannelTag"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioChannelTag) -> list:
    import capo_mediaconvert.types.audio_channel_tag

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.audio_channel_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioChannelTag:
    import capo_mediaconvert.types.audio_channel_tag

    out: __listOfAudioChannelTag = []
    for item in data:
        out.append(capo_mediaconvert.types.audio_channel_tag.deserialize_json(item))
    return out
