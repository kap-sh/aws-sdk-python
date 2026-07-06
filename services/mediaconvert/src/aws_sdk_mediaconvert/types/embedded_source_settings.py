"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EmbeddedSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max1
    import aws_sdk_mediaconvert.types.__integer_min1_max4
    import aws_sdk_mediaconvert.types.embedded_convert608_to708
    import aws_sdk_mediaconvert.types.embedded_terminate_captions


class EmbeddedSourceSettings(TypedDict, closed=True):
    convert608_to708: NotRequired[
        "aws_sdk_mediaconvert.types.embedded_convert608_to708.EmbeddedConvert608To708"
    ]
    """Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708."""
    source608_channel_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """Specifies the 608/708 channel number within the video track from which to extract captions. Unused for passthrough."""
    source608_track_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max1.__integerMin1Max1"
    ]
    """Specifies the video track index used for extracting captions. The system only supports one input video track, so this should always be set to '1'."""
    terminate_captions: NotRequired[
        "aws_sdk_mediaconvert.types.embedded_terminate_captions.EmbeddedTerminateCaptions"
    ]
    """By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedSourceSettings) -> dict:
    out: dict = {}
    if "convert608_to708" in value:
        import aws_sdk_mediaconvert.types.embedded_convert608_to708

        out["convert608To708"] = (
            aws_sdk_mediaconvert.types.embedded_convert608_to708.serialize_json(
                value["convert608_to708"]
            )
        )
    if "source608_channel_number" in value:
        out["source608ChannelNumber"] = value["source608_channel_number"]
    if "source608_track_number" in value:
        out["source608TrackNumber"] = value["source608_track_number"]
    if "terminate_captions" in value:
        import aws_sdk_mediaconvert.types.embedded_terminate_captions

        out["terminateCaptions"] = (
            aws_sdk_mediaconvert.types.embedded_terminate_captions.serialize_json(
                value["terminate_captions"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmbeddedSourceSettings:
    out: EmbeddedSourceSettings = {}  # type: ignore[typeddict-item]
    if "convert608To708" in data:
        import aws_sdk_mediaconvert.types.embedded_convert608_to708

        out["convert608_to708"] = (
            aws_sdk_mediaconvert.types.embedded_convert608_to708.deserialize_json(
                data["convert608To708"]
            )
        )
    if "source608ChannelNumber" in data:
        out["source608_channel_number"] = data["source608ChannelNumber"]
    if "source608TrackNumber" in data:
        out["source608_track_number"] = data["source608TrackNumber"]
    if "terminateCaptions" in data:
        import aws_sdk_mediaconvert.types.embedded_terminate_captions

        out["terminate_captions"] = (
            aws_sdk_mediaconvert.types.embedded_terminate_captions.deserialize_json(
                data["terminateCaptions"]
            )
        )
    return out
