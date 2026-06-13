"""Generated from Smithy shape ``com.amazonaws.qbusiness#VideoExtractionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.video_extraction_status


class VideoExtractionConfiguration(TypedDict):
    video_extraction_status: (
        "aws_sdk_qbusiness.types.video_extraction_status.VideoExtractionStatus"
    )
    """<p>The status of video extraction (ENABLED or DISABLED) for processing video content from files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.video_extraction_status

    out["videoExtractionStatus"] = (
        aws_sdk_qbusiness.types.video_extraction_status.serialize_json(
            value["video_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoExtractionConfiguration:
    out: VideoExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "videoExtractionStatus" in data:
        import aws_sdk_qbusiness.types.video_extraction_status

        out["video_extraction_status"] = (
            aws_sdk_qbusiness.types.video_extraction_status.deserialize_json(
                data["videoExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "VideoExtractionConfiguration.video_extraction_status required"
        )
    return out
