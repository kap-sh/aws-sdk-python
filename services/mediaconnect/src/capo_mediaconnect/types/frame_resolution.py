"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FrameResolution``."""

from typing_extensions import NotRequired, TypedDict


class FrameResolution(TypedDict, closed=True):
    frame_height: NotRequired["int"]
    """<p> The number of pixels in the height of the video frame.</p>"""
    frame_width: NotRequired["int"]
    """<p> The number of pixels in the width of the video frame.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameResolution) -> dict:
    out: dict = {}
    if "frame_height" in value:
        out["frameHeight"] = value["frame_height"]
    if "frame_width" in value:
        out["frameWidth"] = value["frame_width"]
    return out


def deserialize_json(data: dict) -> FrameResolution:
    out: FrameResolution = {}  # type: ignore[typeddict-item]
    if "frameHeight" in data:
        out["frame_height"] = data["frameHeight"]
    if "frameWidth" in data:
        out["frame_width"] = data["frameWidth"]
    return out
