"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputClipping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern010920405090509092090909


class InputClipping(TypedDict, closed=True):
    end_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092090909.__stringPattern010920405090509092090909"
    ]
    """Set End timecode to the end of the portion of the input you are clipping. The frame corresponding to the End timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for timecode source under input settings. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to end six minutes into the video, use 01:06:00:00."""
    start_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092090909.__stringPattern010920405090509092090909"
    ]
    """Set Start timecode to the beginning of the portion of the input you are clipping. The frame corresponding to the Start timecode value is included in the clip. Start timecode or End timecode may be left blank, but not both. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When choosing this value, take into account your setting for Input timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your clip to begin five minutes into the video, use 01:05:00:00."""


# --- restJson1 ser/de ---
def serialize_json(value: InputClipping) -> dict:
    out: dict = {}
    if "end_timecode" in value:
        out["endTimecode"] = value["end_timecode"]
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    return out


def deserialize_json(data: dict) -> InputClipping:
    out: InputClipping = {}  # type: ignore[typeddict-item]
    if "endTimecode" in data:
        out["end_timecode"] = data["endTimecode"]
    if "startTimecode" in data:
        out["start_timecode"] = data["startTimecode"]
    return out
