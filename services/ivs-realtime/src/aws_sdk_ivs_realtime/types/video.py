"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#Video``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.bitrate
    import aws_sdk_ivs_realtime.types.framerate
    import aws_sdk_ivs_realtime.types.height
    import aws_sdk_ivs_realtime.types.width


class Video(TypedDict):
    width: NotRequired["aws_sdk_ivs_realtime.types.width.Width"]
    """<p>Video-resolution width. This must be an even number. Note that the maximum value is determined by <code>width</code> times <code>height</code>, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.</p>"""
    height: NotRequired["aws_sdk_ivs_realtime.types.height.Height"]
    """<p>Video-resolution height. This must be an even number. Note that the maximum value is determined by <code>width</code> times <code>height</code>, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.</p>"""
    framerate: NotRequired["aws_sdk_ivs_realtime.types.framerate.Framerate"]
    """<p>Video frame rate, in fps. Default: 30.</p>"""
    bitrate: NotRequired["aws_sdk_ivs_realtime.types.bitrate.Bitrate"]
    """<p>Bitrate for generated output, in bps. Default: 2500000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Video) -> dict:
    out: dict = {}
    if "width" in value:
        out["width"] = value["width"]
    if "height" in value:
        out["height"] = value["height"]
    if "framerate" in value:
        out["framerate"] = value["framerate"]
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    return out


def deserialize_json(data: dict) -> Video:
    out: Video = {}  # type: ignore[typeddict-item]
    if "width" in data:
        out["width"] = data["width"]
    if "height" in data:
        out["height"] = data["height"]
    if "framerate" in data:
        out["framerate"] = data["framerate"]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    return out
