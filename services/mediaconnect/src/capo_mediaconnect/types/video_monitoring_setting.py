"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VideoMonitoringSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.black_frames
    import capo_mediaconnect.types.frozen_frames


class VideoMonitoringSetting(TypedDict, closed=True):
    black_frames: NotRequired["capo_mediaconnect.types.black_frames.BlackFrames"]
    """<p>Detects video frames that are black. </p>"""
    frozen_frames: NotRequired["capo_mediaconnect.types.frozen_frames.FrozenFrames"]
    """<p>Detects video frames that have not changed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoMonitoringSetting) -> dict:
    out: dict = {}
    if "black_frames" in value:
        import capo_mediaconnect.types.black_frames

        out["blackFrames"] = capo_mediaconnect.types.black_frames.serialize_json(
            value["black_frames"]
        )
    if "frozen_frames" in value:
        import capo_mediaconnect.types.frozen_frames

        out["frozenFrames"] = capo_mediaconnect.types.frozen_frames.serialize_json(
            value["frozen_frames"]
        )
    return out


def deserialize_json(data: dict) -> VideoMonitoringSetting:
    out: VideoMonitoringSetting = {}  # type: ignore[typeddict-item]
    if "blackFrames" in data:
        import capo_mediaconnect.types.black_frames

        out["black_frames"] = capo_mediaconnect.types.black_frames.deserialize_json(
            data["blackFrames"]
        )
    if "frozenFrames" in data:
        import capo_mediaconnect.types.frozen_frames

        out["frozen_frames"] = capo_mediaconnect.types.frozen_frames.deserialize_json(
            data["frozenFrames"]
        )
    return out
