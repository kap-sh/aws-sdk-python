"""Generated from Smithy shape ``com.amazonaws.qbusiness#VideoExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.video_extraction_status


class VideoExtractionConfiguration(TypedDict, closed=True):
    video_extraction_status: (
        "capo_qbusiness.types.video_extraction_status.VideoExtractionStatus"
    )
    """<p>The status of video extraction (ENABLED or DISABLED) for processing video content from files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.video_extraction_status

    out["videoExtractionStatus"] = (
        capo_qbusiness.types.video_extraction_status.serialize_json(
            value["video_extraction_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoExtractionConfiguration:
    out: VideoExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if "videoExtractionStatus" in data:
        import capo_qbusiness.types.video_extraction_status

        out["video_extraction_status"] = (
            capo_qbusiness.types.video_extraction_status.deserialize_json(
                data["videoExtractionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "VideoExtractionConfiguration.video_extraction_status required"
        )
    return out
