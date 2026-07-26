"""Generated from Smithy shape ``com.amazonaws.medialive#VideoBlackFailoverSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min0_max1
    import capo_medialive.types.__integer_min1000


class VideoBlackFailoverSettings(TypedDict, closed=True):
    black_detect_threshold: NotRequired[
        "capo_medialive.types.__double_min0_max1.__doubleMin0Max1"
    ]
    """A value used in calculating the threshold below which MediaLive considers a pixel to be 'black'. For the input to be considered black, every pixel in a frame must be below this threshold. The threshold is calculated as a percentage (expressed as a decimal) of white. Therefore .1 means 10% white (or 90% black). Note how the formula works for any color depth. For example, if you set this field to 0.1 in 10-bit color depth: (1023*0.1=102.3), which means a pixel value of 102 or less is 'black'. If you set this field to .1 in an 8-bit color depth: (255*0.1=25.5), which means a pixel value of 25 or less is 'black'. The range is 0.0 to 1.0, with any number of decimal places."""
    video_black_threshold_msec: NotRequired[
        "capo_medialive.types.__integer_min1000.__integerMin1000"
    ]
    """The amount of time (in milliseconds) that the active input must be black before automatic input failover occurs."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoBlackFailoverSettings) -> dict:
    out: dict = {}
    if "black_detect_threshold" in value:
        out["blackDetectThreshold"] = value["black_detect_threshold"]
    if "video_black_threshold_msec" in value:
        out["videoBlackThresholdMsec"] = value["video_black_threshold_msec"]
    return out


def deserialize_json(data: dict) -> VideoBlackFailoverSettings:
    out: VideoBlackFailoverSettings = {}  # type: ignore[typeddict-item]
    if "blackDetectThreshold" in data:
        out["black_detect_threshold"] = data["blackDetectThreshold"]
    if "videoBlackThresholdMsec" in data:
        out["video_black_threshold_msec"] = data["videoBlackThresholdMsec"]
    return out
