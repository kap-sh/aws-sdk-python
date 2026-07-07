"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AncillarySourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max4
    import aws_sdk_mediaconvert.types.ancillary_convert608_to708
    import aws_sdk_mediaconvert.types.ancillary_terminate_captions


class AncillarySourceSettings(TypedDict, closed=True):
    convert608_to708: NotRequired[
        "aws_sdk_mediaconvert.types.ancillary_convert608_to708.AncillaryConvert608To708"
    ]
    """Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708."""
    source_ancillary_channel_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Specifies the 608 channel number in the ancillary data track from which to extract captions. Unused for passthrough."""
    terminate_captions: NotRequired[
        "aws_sdk_mediaconvert.types.ancillary_terminate_captions.AncillaryTerminateCaptions"
    ]
    """By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: AncillarySourceSettings) -> dict:
    out: dict = {}
    if "convert608_to708" in value:
        import aws_sdk_mediaconvert.types.ancillary_convert608_to708

        out["convert608To708"] = (
            aws_sdk_mediaconvert.types.ancillary_convert608_to708.serialize_json(
                value["convert608_to708"]
            )
        )
    if "source_ancillary_channel_number" in value:
        out["sourceAncillaryChannelNumber"] = value["source_ancillary_channel_number"]
    if "terminate_captions" in value:
        import aws_sdk_mediaconvert.types.ancillary_terminate_captions

        out["terminateCaptions"] = (
            aws_sdk_mediaconvert.types.ancillary_terminate_captions.serialize_json(
                value["terminate_captions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AncillarySourceSettings:
    out: AncillarySourceSettings = {}  # type: ignore[typeddict-item]
    if "convert608To708" in data:
        import aws_sdk_mediaconvert.types.ancillary_convert608_to708

        out["convert608_to708"] = (
            aws_sdk_mediaconvert.types.ancillary_convert608_to708.deserialize_json(
                data["convert608To708"]
            )
        )
    if "sourceAncillaryChannelNumber" in data:
        out["source_ancillary_channel_number"] = data["sourceAncillaryChannelNumber"]
    if "terminateCaptions" in data:
        import aws_sdk_mediaconvert.types.ancillary_terminate_captions

        out["terminate_captions"] = (
            aws_sdk_mediaconvert.types.ancillary_terminate_captions.deserialize_json(
                data["terminateCaptions"]
            )
        )
    return out
