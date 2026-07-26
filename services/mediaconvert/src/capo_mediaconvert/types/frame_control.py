"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FrameControl``."""

from typing import Literal, TypeAlias, cast

"""Choose how MediaConvert handles start and end times for input clipping with video passthrough. Your input video codec must be H.264 or H.265 to use IFRAME. To clip at the nearest IDR-frame: Choose Nearest IDR. If an IDR-frame is not found at the frame that you specify, MediaConvert uses the next compatible IDR-frame. Note that your output may be shorter than your input clip duration. To clip at the nearest I-frame: Choose Nearest I-frame. If an I-frame is not found at the frame that you specify, MediaConvert uses the next compatible I-frame. Note that your output may be shorter than your input clip duration. We only recommend this setting for special workflows, and when you choose this setting your output may not be compatible with most players."""
FrameControl: TypeAlias = Literal[
    "NEAREST_IDRFRAME",
    "NEAREST_IFRAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameControl) -> str:
    return value


def deserialize_json(data: str) -> FrameControl:
    return cast(FrameControl, data)
