"""Generated from Smithy shape ``com.amazonaws.medialive#Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_min1_max255
    import aws_sdk_medialive.types.output_settings


class Output(TypedDict, closed=True):
    audio_description_names: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The names of the AudioDescriptions used as audio sources for this output."""
    caption_description_names: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The names of the CaptionDescriptions used as caption sources for this output."""
    output_name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max255.__stringMin1Max255"
    ]
    """The name used to identify an output."""
    output_settings: NotRequired[
        "aws_sdk_medialive.types.output_settings.OutputSettings"
    ]
    """Output type-specific settings."""
    video_description_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the VideoDescription used as the source for this output."""


# --- restJson1 ser/de ---
def serialize_json(value: Output) -> dict:
    out: dict = {}
    if "audio_description_names" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["audioDescriptionNames"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["audio_description_names"]
            )
        )
    if "caption_description_names" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["captionDescriptionNames"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["caption_description_names"]
            )
        )
    if "output_name" in value:
        out["outputName"] = value["output_name"]
    if "output_settings" in value:
        import aws_sdk_medialive.types.output_settings

        out["outputSettings"] = aws_sdk_medialive.types.output_settings.serialize_json(
            value["output_settings"]
        )
    if "video_description_name" in value:
        out["videoDescriptionName"] = value["video_description_name"]
    return out


def deserialize_json(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if "audioDescriptionNames" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["audio_description_names"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["audioDescriptionNames"]
            )
        )
    if "captionDescriptionNames" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["caption_description_names"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["captionDescriptionNames"]
            )
        )
    if "outputName" in data:
        out["output_name"] = data["outputName"]
    if "outputSettings" in data:
        import aws_sdk_medialive.types.output_settings

        out["output_settings"] = (
            aws_sdk_medialive.types.output_settings.deserialize_json(
                data["outputSettings"]
            )
        )
    if "videoDescriptionName" in data:
        out["video_description_name"] = data["videoDescriptionName"]
    return out
