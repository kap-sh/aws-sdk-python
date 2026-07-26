"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioChannelTaggingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_audio_channel_tag
    import capo_mediaconvert.types.audio_channel_tag


class AudioChannelTaggingSettings(TypedDict, closed=True):
    channel_tag: NotRequired[
        "capo_mediaconvert.types.audio_channel_tag.AudioChannelTag"
    ]
    """Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track."""
    channel_tags: NotRequired[
        "capo_mediaconvert.types.__list_of_audio_channel_tag.__listOfAudioChannelTag"
    ]
    """Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioChannelTaggingSettings) -> dict:
    out: dict = {}
    if "channel_tag" in value:
        import capo_mediaconvert.types.audio_channel_tag

        out["channelTag"] = capo_mediaconvert.types.audio_channel_tag.serialize_json(
            value["channel_tag"]
        )
    if "channel_tags" in value:
        import capo_mediaconvert.types.__list_of_audio_channel_tag

        out["channelTags"] = (
            capo_mediaconvert.types.__list_of_audio_channel_tag.serialize_json(
                value["channel_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioChannelTaggingSettings:
    out: AudioChannelTaggingSettings = {}  # type: ignore[typeddict-item]
    if "channelTag" in data:
        import capo_mediaconvert.types.audio_channel_tag

        out["channel_tag"] = capo_mediaconvert.types.audio_channel_tag.deserialize_json(
            data["channelTag"]
        )
    if "channelTags" in data:
        import capo_mediaconvert.types.__list_of_audio_channel_tag

        out["channel_tags"] = (
            capo_mediaconvert.types.__list_of_audio_channel_tag.deserialize_json(
                data["channelTags"]
            )
        )
    return out
