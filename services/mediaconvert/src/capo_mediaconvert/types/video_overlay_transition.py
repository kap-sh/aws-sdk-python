"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern010920405090509092
    import capo_mediaconvert.types.video_overlay_position


class VideoOverlayTransition(TypedDict, closed=True):
    end_position: NotRequired[
        "capo_mediaconvert.types.video_overlay_position.VideoOverlayPosition"
    ]
    """Specify the ending position for this transition, relative to the base input video's frame. Your video overlay will move smoothly to this position, beginning at this transition's Start timecode and ending at this transition's End timecode."""
    end_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Specify the timecode for when this transition ends. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source."""
    start_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Specify the timecode for when this transition begins. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for Timecode source."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayTransition) -> dict:
    out: dict = {}
    if "end_position" in value:
        import capo_mediaconvert.types.video_overlay_position

        out["endPosition"] = (
            capo_mediaconvert.types.video_overlay_position.serialize_json(
                value["end_position"]
            )
        )
    if "end_timecode" in value:
        out["endTimecode"] = value["end_timecode"]
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    return out


def deserialize_json(data: dict) -> VideoOverlayTransition:
    out: VideoOverlayTransition = {}  # type: ignore[typeddict-item]
    if "endPosition" in data:
        import capo_mediaconvert.types.video_overlay_position

        out["end_position"] = (
            capo_mediaconvert.types.video_overlay_position.deserialize_json(
                data["endPosition"]
            )
        )
    if "endTimecode" in data:
        out["end_timecode"] = data["endTimecode"]
    if "startTimecode" in data:
        out["start_timecode"] = data["startTimecode"]
    return out
