"""Generated from Smithy shape ``com.amazonaws.medialive#AudioChannelMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max7
    import aws_sdk_medialive.types.__list_of_input_channel_level


class AudioChannelMapping(TypedDict):
    input_channel_levels: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_channel_level.__listOfInputChannelLevel"
    ]
    """Indices and gain values for each input channel that should be remixed into this output channel."""
    output_channel: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max7.__integerMin0Max7"
    ]
    """The index of the output channel being produced."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioChannelMapping) -> dict:
    out: dict = {}
    if "input_channel_levels" in value:
        import aws_sdk_medialive.types.__list_of_input_channel_level

        out["inputChannelLevels"] = (
            aws_sdk_medialive.types.__list_of_input_channel_level.serialize_json(
                value["input_channel_levels"]
            )
        )
    if "output_channel" in value:
        out["outputChannel"] = value["output_channel"]
    return out


def deserialize_json(data: dict) -> AudioChannelMapping:
    out: AudioChannelMapping = {}  # type: ignore[typeddict-item]
    if "inputChannelLevels" in data:
        import aws_sdk_medialive.types.__list_of_input_channel_level

        out["input_channel_levels"] = (
            aws_sdk_medialive.types.__list_of_input_channel_level.deserialize_json(
                data["inputChannelLevels"]
            )
        )
    if "outputChannel" in data:
        out["output_channel"] = data["outputChannel"]
    return out
