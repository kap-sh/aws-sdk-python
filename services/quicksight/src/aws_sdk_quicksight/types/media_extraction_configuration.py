"""Generated from Smithy shape ``com.amazonaws.quicksight#MediaExtractionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.audio_extraction_configuration
    import aws_sdk_quicksight.types.image_extraction_configuration
    import aws_sdk_quicksight.types.video_extraction_configuration


class MediaExtractionConfiguration(TypedDict):
    image_extraction_configuration: NotRequired[
        "aws_sdk_quicksight.types.image_extraction_configuration.ImageExtractionConfiguration"
    ]
    """<p>The configuration for image extraction.</p>"""
    audio_extraction_configuration: NotRequired[
        "aws_sdk_quicksight.types.audio_extraction_configuration.AudioExtractionConfiguration"
    ]
    """<p>The configuration for audio extraction.</p>"""
    video_extraction_configuration: NotRequired[
        "aws_sdk_quicksight.types.video_extraction_configuration.VideoExtractionConfiguration"
    ]
    """<p>The configuration for video extraction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaExtractionConfiguration) -> dict:
    out: dict = {}
    if "image_extraction_configuration" in value:
        import aws_sdk_quicksight.types.image_extraction_configuration

        out["imageExtractionConfiguration"] = (
            aws_sdk_quicksight.types.image_extraction_configuration.serialize_json(
                value["image_extraction_configuration"]
            )
        )
    if "audio_extraction_configuration" in value:
        import aws_sdk_quicksight.types.audio_extraction_configuration

        out["audioExtractionConfiguration"] = (
            aws_sdk_quicksight.types.audio_extraction_configuration.serialize_json(
                value["audio_extraction_configuration"]
            )
        )
    if "video_extraction_configuration" in value:
        import aws_sdk_quicksight.types.video_extraction_configuration

        out["videoExtractionConfiguration"] = (
            aws_sdk_quicksight.types.video_extraction_configuration.serialize_json(
                value["video_extraction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaExtractionConfiguration:
    out: MediaExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "imageExtractionConfiguration" in data:
        import aws_sdk_quicksight.types.image_extraction_configuration

        out["image_extraction_configuration"] = (
            aws_sdk_quicksight.types.image_extraction_configuration.deserialize_json(
                data["imageExtractionConfiguration"]
            )
        )
    if "audioExtractionConfiguration" in data:
        import aws_sdk_quicksight.types.audio_extraction_configuration

        out["audio_extraction_configuration"] = (
            aws_sdk_quicksight.types.audio_extraction_configuration.deserialize_json(
                data["audioExtractionConfiguration"]
            )
        )
    if "videoExtractionConfiguration" in data:
        import aws_sdk_quicksight.types.video_extraction_configuration

        out["video_extraction_configuration"] = (
            aws_sdk_quicksight.types.video_extraction_configuration.deserialize_json(
                data["videoExtractionConfiguration"]
            )
        )
    return out
