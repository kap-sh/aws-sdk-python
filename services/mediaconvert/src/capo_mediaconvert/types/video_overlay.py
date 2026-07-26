"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlay``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_video_overlay_transition
    import capo_mediaconvert.types.__string_pattern010920405090509092
    import capo_mediaconvert.types.video_overlay_crop
    import capo_mediaconvert.types.video_overlay_input
    import capo_mediaconvert.types.video_overlay_play_back_mode
    import capo_mediaconvert.types.video_overlay_position


class VideoOverlay(TypedDict, closed=True):
    crop: NotRequired["capo_mediaconvert.types.video_overlay_crop.VideoOverlayCrop"]
    """Specify a rectangle of content to crop and use from your video overlay's input video. When you do, MediaConvert uses the cropped dimensions that you specify under X offset, Y offset, Width, and Height."""
    end_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Enter the end timecode in the base input video for this overlay. Your overlay will be active through this frame. To display your video overlay for the duration of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS isthe second, and FF is the frame number. When entering this value, take into account your choice for the base input video's timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to end ten minutes into the video, enter 01:10:00:00."""
    initial_position: NotRequired[
        "capo_mediaconvert.types.video_overlay_position.VideoOverlayPosition"
    ]
    """Specify the Initial position of your video overlay. To specify the Initial position of your video overlay, including distance from the left or top edge of the base input video's frame, or size: Enter a value for X position, Y position, Width, or Height. To use the full frame of the base input video: Leave blank."""
    input: NotRequired["capo_mediaconvert.types.video_overlay_input.VideoOverlayInput"]
    """Input settings for Video overlay. You can include one or more video overlays in sequence at different times that you specify."""
    playback: NotRequired[
        "capo_mediaconvert.types.video_overlay_play_back_mode.VideoOverlayPlayBackMode"
    ]
    """Specify whether your video overlay repeats or plays only once. To repeat your video overlay on a loop: Keep the default value, Repeat. Your overlay will repeat for the duration of the base input video. To playback your video overlay only once: Choose Once. With either option, you can end playback at a time that you specify by entering a value for End timecode."""
    start_timecode: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Enter the start timecode in the base input video for this overlay. Your overlay will be active starting with this frame. To display your video overlay starting at the beginning of the base input video: Leave blank. Use the format HH:MM:SS:FF or HH:MM:SS;FF, where HH is the hour, MM is the minute, SS is the second, and FF is the frame number. When entering this value, take into account your choice for the base input video's timecode source. For example, if you have embedded timecodes that start at 01:00:00:00 and you want your overlay to begin five minutes into the video, enter 01:05:00:00."""
    transitions: NotRequired[
        "capo_mediaconvert.types.__list_of_video_overlay_transition.__listOfVideoOverlayTransition"
    ]
    """Specify one or more transitions for your video overlay. Use Transitions to reposition or resize your overlay over time. To use the same position and size for the duration of your video overlay: Leave blank. To specify a Transition: Enter a value for Start timecode, End Timecode, X Position, Y Position, Width, or Height."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlay) -> dict:
    out: dict = {}
    if "crop" in value:
        import capo_mediaconvert.types.video_overlay_crop

        out["crop"] = capo_mediaconvert.types.video_overlay_crop.serialize_json(
            value["crop"]
        )
    if "end_timecode" in value:
        out["endTimecode"] = value["end_timecode"]
    if "initial_position" in value:
        import capo_mediaconvert.types.video_overlay_position

        out["initialPosition"] = (
            capo_mediaconvert.types.video_overlay_position.serialize_json(
                value["initial_position"]
            )
        )
    if "input" in value:
        import capo_mediaconvert.types.video_overlay_input

        out["input"] = capo_mediaconvert.types.video_overlay_input.serialize_json(
            value["input"]
        )
    if "playback" in value:
        import capo_mediaconvert.types.video_overlay_play_back_mode

        out["playback"] = (
            capo_mediaconvert.types.video_overlay_play_back_mode.serialize_json(
                value["playback"]
            )
        )
    if "start_timecode" in value:
        out["startTimecode"] = value["start_timecode"]
    if "transitions" in value:
        import capo_mediaconvert.types.__list_of_video_overlay_transition

        out["transitions"] = (
            capo_mediaconvert.types.__list_of_video_overlay_transition.serialize_json(
                value["transitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoOverlay:
    out: VideoOverlay = {}  # type: ignore[typeddict-item]
    if "crop" in data:
        import capo_mediaconvert.types.video_overlay_crop

        out["crop"] = capo_mediaconvert.types.video_overlay_crop.deserialize_json(
            data["crop"]
        )
    if "endTimecode" in data:
        out["end_timecode"] = data["endTimecode"]
    if "initialPosition" in data:
        import capo_mediaconvert.types.video_overlay_position

        out["initial_position"] = (
            capo_mediaconvert.types.video_overlay_position.deserialize_json(
                data["initialPosition"]
            )
        )
    if "input" in data:
        import capo_mediaconvert.types.video_overlay_input

        out["input"] = capo_mediaconvert.types.video_overlay_input.deserialize_json(
            data["input"]
        )
    if "playback" in data:
        import capo_mediaconvert.types.video_overlay_play_back_mode

        out["playback"] = (
            capo_mediaconvert.types.video_overlay_play_back_mode.deserialize_json(
                data["playback"]
            )
        )
    if "startTimecode" in data:
        out["start_timecode"] = data["startTimecode"]
    if "transitions" in data:
        import capo_mediaconvert.types.__list_of_video_overlay_transition

        out["transitions"] = (
            capo_mediaconvert.types.__list_of_video_overlay_transition.deserialize_json(
                data["transitions"]
            )
        )
    return out
