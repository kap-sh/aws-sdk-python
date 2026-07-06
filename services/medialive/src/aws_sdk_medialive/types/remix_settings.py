"""Generated from Smithy shape ``com.amazonaws.medialive#RemixSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1_max8
    import aws_sdk_medialive.types.__integer_min1_max16
    import aws_sdk_medialive.types.__list_of_audio_channel_mapping


class RemixSettings(TypedDict, closed=True):
    channel_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_audio_channel_mapping.__listOfAudioChannelMapping"
    ]
    """Mapping of input channels to output channels, with appropriate gain adjustments."""
    channels_in: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max16.__integerMin1Max16"
    ]
    """Number of input channels to be used."""
    channels_out: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max8.__integerMin1Max8"
    ]
    """Number of output channels to be produced. Valid values: 1, 2, 4, 6, 8"""


# --- restJson1 ser/de ---
def serialize_json(value: RemixSettings) -> dict:
    out: dict = {}
    if "channel_mappings" in value:
        import aws_sdk_medialive.types.__list_of_audio_channel_mapping

        out["channelMappings"] = (
            aws_sdk_medialive.types.__list_of_audio_channel_mapping.serialize_json(
                value["channel_mappings"]
            )
        )
    if "channels_in" in value:
        out["channelsIn"] = value["channels_in"]
    if "channels_out" in value:
        out["channelsOut"] = value["channels_out"]
    return out


def deserialize_json(data: dict) -> RemixSettings:
    out: RemixSettings = {}  # type: ignore[typeddict-item]
    if "channelMappings" in data:
        import aws_sdk_medialive.types.__list_of_audio_channel_mapping

        out["channel_mappings"] = (
            aws_sdk_medialive.types.__list_of_audio_channel_mapping.deserialize_json(
                data["channelMappings"]
            )
        )
    if "channelsIn" in data:
        out["channels_in"] = data["channelsIn"]
    if "channelsOut" in data:
        out["channels_out"] = data["channelsOut"]
    return out
