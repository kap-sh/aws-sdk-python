"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.video_detail


class OutputDetail(TypedDict, closed=True):
    duration_in_ms: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """Duration in milliseconds"""
    video_details: NotRequired["capo_mediaconvert.types.video_detail.VideoDetail"]
    """Contains details about the output's video stream"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDetail) -> dict:
    out: dict = {}
    if "duration_in_ms" in value:
        out["durationInMs"] = value["duration_in_ms"]
    if "video_details" in value:
        import capo_mediaconvert.types.video_detail

        out["videoDetails"] = capo_mediaconvert.types.video_detail.serialize_json(
            value["video_details"]
        )
    return out


def deserialize_json(data: dict) -> OutputDetail:
    out: OutputDetail = {}  # type: ignore[typeddict-item]
    if "durationInMs" in data:
        out["duration_in_ms"] = data["durationInMs"]
    if "videoDetails" in data:
        import capo_mediaconvert.types.video_detail

        out["video_details"] = capo_mediaconvert.types.video_detail.deserialize_json(
            data["videoDetails"]
        )
    return out
