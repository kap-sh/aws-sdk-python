"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.video_detail


class OutputDetail(TypedDict):
    duration_in_ms: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Duration in milliseconds"""
    video_details: NotRequired["aws_sdk_mediaconvert.types.video_detail.VideoDetail"]
    """Contains details about the output's video stream"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDetail) -> dict:
    out: dict = {}
    if "duration_in_ms" in value:
        out["durationInMs"] = value["duration_in_ms"]
    if "video_details" in value:
        import aws_sdk_mediaconvert.types.video_detail

        out["videoDetails"] = aws_sdk_mediaconvert.types.video_detail.serialize_json(
            value["video_details"]
        )
    return out


def deserialize_json(data: dict) -> OutputDetail:
    out: OutputDetail = {}  # type: ignore[typeddict-item]
    if "durationInMs" in data:
        out["duration_in_ms"] = data["durationInMs"]
    if "videoDetails" in data:
        import aws_sdk_mediaconvert.types.video_detail

        out["video_details"] = aws_sdk_mediaconvert.types.video_detail.deserialize_json(
            data["videoDetails"]
        )
    return out
