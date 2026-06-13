"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VideoMonitoringSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.black_frames
    import aws_sdk_mediaconnect.types.frozen_frames


class VideoMonitoringSetting(TypedDict):
    black_frames: NotRequired["aws_sdk_mediaconnect.types.black_frames.BlackFrames"]
    """<p>Detects video frames that are black. </p>"""
    frozen_frames: NotRequired["aws_sdk_mediaconnect.types.frozen_frames.FrozenFrames"]
    """<p>Detects video frames that have not changed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoMonitoringSetting) -> dict:
    out: dict = {}
    if "black_frames" in value:
        import aws_sdk_mediaconnect.types.black_frames

        out["blackFrames"] = aws_sdk_mediaconnect.types.black_frames.serialize_json(
            value["black_frames"]
        )
    if "frozen_frames" in value:
        import aws_sdk_mediaconnect.types.frozen_frames

        out["frozenFrames"] = aws_sdk_mediaconnect.types.frozen_frames.serialize_json(
            value["frozen_frames"]
        )
    return out


def deserialize_json(data: dict) -> VideoMonitoringSetting:
    out: VideoMonitoringSetting = {}  # type: ignore[typeddict-item]
    if "blackFrames" in data:
        import aws_sdk_mediaconnect.types.black_frames

        out["black_frames"] = aws_sdk_mediaconnect.types.black_frames.deserialize_json(
            data["blackFrames"]
        )
    if "frozenFrames" in data:
        import aws_sdk_mediaconnect.types.frozen_frames

        out["frozen_frames"] = (
            aws_sdk_mediaconnect.types.frozen_frames.deserialize_json(
                data["frozenFrames"]
            )
        )
    return out
