"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionSynchronizationMode``."""

from typing import Literal, TypeAlias, cast

"""Controls how MediaLive synchronizes Elemental Inference generated subtitles with video output. video_aligned_captions - MediaLive delays video to ensure captions are synchronized with audio and video. no_video_delay - MediaLive does not delay video for caption alignment. Captions output timing is adjusted to align with video as captions become available."""
CaptionSynchronizationMode: TypeAlias = Literal[
    "NO_VIDEO_DELAY",
    "VIDEO_ALIGNED_CAPTIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSynchronizationMode) -> str:
    return value


def deserialize_json(data: str) -> CaptionSynchronizationMode:
    return cast(CaptionSynchronizationMode, data)
