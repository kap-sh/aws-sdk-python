"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PassthroughSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.frame_control
    import capo_mediaconvert.types.video_selector_mode


class PassthroughSettings(TypedDict, closed=True):
    frame_control: NotRequired["capo_mediaconvert.types.frame_control.FrameControl"]
    """Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players."""
    video_selector_mode: NotRequired[
        "capo_mediaconvert.types.video_selector_mode.VideoSelectorMode"
    ]
    """AUTO will select the highest bitrate input in the video selector source. REMUX_ALL will passthrough all the selected streams in the video selector source. When selecting streams from multiple renditions (i.e. using Stream video selector type): REMUX_ALL will only remux all streams selected, and AUTO will use the highest bitrate video stream among the selected streams as source."""


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughSettings) -> dict:
    out: dict = {}
    if "frame_control" in value:
        import capo_mediaconvert.types.frame_control

        out["frameControl"] = capo_mediaconvert.types.frame_control.serialize_json(
            value["frame_control"]
        )
    if "video_selector_mode" in value:
        import capo_mediaconvert.types.video_selector_mode

        out["videoSelectorMode"] = (
            capo_mediaconvert.types.video_selector_mode.serialize_json(
                value["video_selector_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> PassthroughSettings:
    out: PassthroughSettings = {}  # type: ignore[typeddict-item]
    if "frameControl" in data:
        import capo_mediaconvert.types.frame_control

        out["frame_control"] = capo_mediaconvert.types.frame_control.deserialize_json(
            data["frameControl"]
        )
    if "videoSelectorMode" in data:
        import capo_mediaconvert.types.video_selector_mode

        out["video_selector_mode"] = (
            capo_mediaconvert.types.video_selector_mode.deserialize_json(
                data["videoSelectorMode"]
            )
        )
    return out
