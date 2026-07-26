"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ChannelMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_output_channel_mapping


class ChannelMapping(TypedDict, closed=True):
    output_channels: NotRequired[
        "capo_mediaconvert.types.__list_of_output_channel_mapping.__listOfOutputChannelMapping"
    ]
    """In your JSON job specification, include one child of OutputChannels for each audio channel that you want in your output. Each child should contain one instance of InputChannels or InputChannelsFineTune."""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMapping) -> dict:
    out: dict = {}
    if "output_channels" in value:
        import capo_mediaconvert.types.__list_of_output_channel_mapping

        out["outputChannels"] = (
            capo_mediaconvert.types.__list_of_output_channel_mapping.serialize_json(
                value["output_channels"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelMapping:
    out: ChannelMapping = {}  # type: ignore[typeddict-item]
    if "outputChannels" in data:
        import capo_mediaconvert.types.__list_of_output_channel_mapping

        out["output_channels"] = (
            capo_mediaconvert.types.__list_of_output_channel_mapping.deserialize_json(
                data["outputChannels"]
            )
        )
    return out
