"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioChannelTaggingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_audio_channel_tag
    import aws_sdk_mediaconvert.types.audio_channel_tag


class AudioChannelTaggingSettings(TypedDict):
    channel_tag: NotRequired[
        "aws_sdk_mediaconvert.types.audio_channel_tag.AudioChannelTag"
    ]
    """Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track."""
    channel_tags: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_audio_channel_tag.__listOfAudioChannelTag"
    ]
    """Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioChannelTaggingSettings) -> dict:
    out: dict = {}
    if "channel_tag" in value:
        import aws_sdk_mediaconvert.types.audio_channel_tag

        out["channelTag"] = aws_sdk_mediaconvert.types.audio_channel_tag.serialize_json(
            value["channel_tag"]
        )
    if "channel_tags" in value:
        import aws_sdk_mediaconvert.types.__list_of_audio_channel_tag

        out["channelTags"] = (
            aws_sdk_mediaconvert.types.__list_of_audio_channel_tag.serialize_json(
                value["channel_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioChannelTaggingSettings:
    out: AudioChannelTaggingSettings = {}  # type: ignore[typeddict-item]
    if "channelTag" in data:
        import aws_sdk_mediaconvert.types.audio_channel_tag

        out["channel_tag"] = (
            aws_sdk_mediaconvert.types.audio_channel_tag.deserialize_json(
                data["channelTag"]
            )
        )
    if "channelTags" in data:
        import aws_sdk_mediaconvert.types.__list_of_audio_channel_tag

        out["channel_tags"] = (
            aws_sdk_mediaconvert.types.__list_of_audio_channel_tag.deserialize_json(
                data["channelTags"]
            )
        )
    return out
