"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.video_extraction_status
    import aws_sdk_quicksight.types.video_extraction_type


class VideoExtractionConfiguration(TypedDict, closed=True):
    video_extraction_status: (
        "aws_sdk_quicksight.types.video_extraction_status.VideoExtractionStatus"
    )
    """<p>The status of video extraction. Valid values are ENABLED and DISABLED.</p>"""
    video_extraction_type: NotRequired[
        "aws_sdk_quicksight.types.video_extraction_type.VideoExtractionType"
    ]
    """<p>The type of video extraction to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.video_extraction_status

    out["videoExtractionStatus"] = (
        aws_sdk_quicksight.types.video_extraction_status.serialize_json(
            value["video_extraction_status"]
        )
    )
    if "video_extraction_type" in value:
        import aws_sdk_quicksight.types.video_extraction_type

        out["videoExtractionType"] = (
            aws_sdk_quicksight.types.video_extraction_type.serialize_json(
                value["video_extraction_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoExtractionConfiguration:
    out: VideoExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "videoExtractionStatus" in data:
        import aws_sdk_quicksight.types.video_extraction_status

        out["video_extraction_status"] = (
            aws_sdk_quicksight.types.video_extraction_status.deserialize_json(
                data["videoExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "VideoExtractionConfiguration.video_extraction_status required"
        )
    if "videoExtractionType" in data:
        import aws_sdk_quicksight.types.video_extraction_type

        out["video_extraction_type"] = (
            aws_sdk_quicksight.types.video_extraction_type.deserialize_json(
                data["videoExtractionType"]
            )
        )
    return out
