"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputChannelMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6
    import aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6


class OutputChannelMapping(TypedDict):
    input_channels: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6.__listOf__integerMinNegative60Max6"
    ]
    """Use this setting to specify your remix values when they are integers, such as -10, 0, or 4."""
    input_channels_fine_tune: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6.__listOf__doubleMinNegative60Max6"
    ]
    """Use this setting to specify your remix values when they have a decimal component, such as -10.312, 0.08, or 4.9. MediaConvert rounds your remixing values to the nearest thousandth."""


# --- restJson1 ser/de ---
def serialize_json(value: OutputChannelMapping) -> dict:
    out: dict = {}
    if "input_channels" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6

        out["inputChannels"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6.serialize_json(
                value["input_channels"]
            )
        )
    if "input_channels_fine_tune" in value:
        import aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6

        out["inputChannelsFineTune"] = (
            aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6.serialize_json(
                value["input_channels_fine_tune"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputChannelMapping:
    out: OutputChannelMapping = {}  # type: ignore[typeddict-item]
    if "inputChannels" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6

        out["input_channels"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min_negative60_max6.deserialize_json(
                data["inputChannels"]
            )
        )
    if "inputChannelsFineTune" in data:
        import aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6

        out["input_channels_fine_tune"] = (
            aws_sdk_mediaconvert.types.__list_of__double_min_negative60_max6.deserialize_json(
                data["inputChannelsFineTune"]
            )
        )
    return out
