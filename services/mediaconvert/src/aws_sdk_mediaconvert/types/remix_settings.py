"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RemixSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max64
    import aws_sdk_mediaconvert.types.channel_mapping


class RemixSettings(TypedDict, closed=True):
    audio_description_audio_channel: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max64.__integerMin1Max64"
    ]
    """Optionally specify the channel in your input that contains your audio description audio signal. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description audio channel, you must also specify an audio description data channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers."""
    audio_description_data_channel: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max64.__integerMin1Max64"
    ]
    """Optionally specify the channel in your input that contains your audio description data stream. MediaConvert mixes your audio signal across all output channels, while reducing their volume according to your data stream. When you specify an audio description data channel, you must also specify an audio description audio channel. For more information about audio description signals, see the BBC WHP 198 and 051 white papers."""
    channel_mapping: NotRequired[
        "aws_sdk_mediaconvert.types.channel_mapping.ChannelMapping"
    ]
    """Channel mapping contains the group of fields that hold the remixing value for each channel, in dB. Specify remix values to indicate how much of the content from your input audio channel you want in your output audio channels. Each instance of the InputChannels or InputChannelsFineTune array specifies these values for one output channel. Use one instance of this array for each output channel. In the console, each array corresponds to a column in the graphical depiction of the mapping matrix. The rows of the graphical matrix correspond to input channels. Valid values are within the range from -60 (mute) through 6. A setting of 0 passes the input channel unchanged to the output channel (no attenuation or amplification). Use InputChannels or InputChannelsFineTune to specify your remix values. Don't use both."""
    channels_in: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max64.__integerMin1Max64"
    ]
    """Specify the number of audio channels from your input that you want to use in your output. With remixing, you might combine or split the data in these channels, so the number of channels in your final output might be different. If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping."""
    channels_out: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max64.__integerMin1Max64"
    ]
    """Specify the number of channels in this output after remixing. Valid values: 1, 2, 4, 6, 8... 64. (1 and even numbers to 64.) If you are doing both input channel mapping and output channel mapping, the number of output channels in your input mapping must be the same as the number of input channels in your output mapping."""


# --- restJson1 ser/de ---
def serialize_json(value: RemixSettings) -> dict:
    out: dict = {}
    if "audio_description_audio_channel" in value:
        out["audioDescriptionAudioChannel"] = value["audio_description_audio_channel"]
    if "audio_description_data_channel" in value:
        out["audioDescriptionDataChannel"] = value["audio_description_data_channel"]
    if "channel_mapping" in value:
        import aws_sdk_mediaconvert.types.channel_mapping

        out["channelMapping"] = (
            aws_sdk_mediaconvert.types.channel_mapping.serialize_json(
                value["channel_mapping"]
            )
        )
    if "channels_in" in value:
        out["channelsIn"] = value["channels_in"]
    if "channels_out" in value:
        out["channelsOut"] = value["channels_out"]
    return out


def deserialize_json(data: dict) -> RemixSettings:
    out: RemixSettings = {}  # type: ignore[typeddict-item]
    if "audioDescriptionAudioChannel" in data:
        out["audio_description_audio_channel"] = data["audioDescriptionAudioChannel"]
    if "audioDescriptionDataChannel" in data:
        out["audio_description_data_channel"] = data["audioDescriptionDataChannel"]
    if "channelMapping" in data:
        import aws_sdk_mediaconvert.types.channel_mapping

        out["channel_mapping"] = (
            aws_sdk_mediaconvert.types.channel_mapping.deserialize_json(
                data["channelMapping"]
            )
        )
    if "channelsIn" in data:
        out["channels_in"] = data["channelsIn"]
    if "channelsOut" in data:
        out["channels_out"] = data["channelsOut"]
    return out
