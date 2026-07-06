"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayInputClipping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern010920405090509092090909


class VideoOverlayInputClipping(TypedDict, closed=True):
    end_timecode: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern010920405090509092090909.__stringPattern010920405090509092090909"
    ]
    """Specify the timecode of the last frame to include in your video overlay's clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source."""
    start_timecode: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern010920405090509092090909.__stringPattern010920405090509092090909"
    ]
    """Specify the timecode of the first frame to include in your video overlay's clip. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayInputClipping) -> dict:
    out: dict = {}
    if "end_timecode" in value:
        out["endTimecode"] = value["end_timecode"]
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    return out


def deserialize_json(data: dict) -> VideoOverlayInputClipping:
    out: VideoOverlayInputClipping = {}  # type: ignore[typeddict-item]
    if "endTimecode" in data:
        out["end_timecode"] = data["endTimecode"]
    if "startTimecode" in data:
        out["start_timecode"] = data["startTimecode"]
    return out
