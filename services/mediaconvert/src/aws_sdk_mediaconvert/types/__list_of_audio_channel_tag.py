"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfAudioChannelTag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.audio_channel_tag

__listOfAudioChannelTag: TypeAlias = list[
    "aws_sdk_mediaconvert.types.audio_channel_tag.AudioChannelTag"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioChannelTag) -> list:
    import aws_sdk_mediaconvert.types.audio_channel_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.audio_channel_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioChannelTag:
    import aws_sdk_mediaconvert.types.audio_channel_tag

    out: __listOfAudioChannelTag = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.audio_channel_tag.deserialize_json(item))
    return out
