"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EmbeddedDestinationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max4
    import aws_sdk_mediaconvert.types.__integer_min1_max6


class EmbeddedDestinationSettings(TypedDict):
    destination608_channel_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Ignore this setting unless your input captions are SCC format and your output captions are embedded in the video stream. Specify a CC number for each captions channel in this output. If you have two channels, choose CC numbers that aren't in the same field. For example, choose 1 and 3. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded."""
    destination708_service_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max6.__integerMin1Max6"
    ]
    """Ignore this setting unless your input captions are SCC format and you want both 608 and 708 captions embedded in your output stream. Optionally, specify the 708 service number for each output captions channel. Choose a different number for each channel. To use this setting, also set Force 608 to 708 upconvert to Upconvert in your input captions selector settings. If you choose to upconvert but don't specify a 708 service number, MediaConvert uses the number that you specify for CC channel number for the 708 service number. For more information, see https://docs.aws.amazon.com/console/mediaconvert/dual-scc-to-embedded."""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedDestinationSettings) -> dict:
    out: dict = {}
    if "destination608_channel_number" in value:
        out["destination608ChannelNumber"] = value["destination608_channel_number"]
    if "destination708_service_number" in value:
        out["destination708ServiceNumber"] = value["destination708_service_number"]
    return out


def deserialize_json(data: dict) -> EmbeddedDestinationSettings:
    out: EmbeddedDestinationSettings = {}  # type: ignore[typeddict-item]
    if "destination608ChannelNumber" in data:
        out["destination608_channel_number"] = data["destination608ChannelNumber"]
    if "destination708ServiceNumber" in data:
        out["destination708_service_number"] = data["destination708ServiceNumber"]
    return out
