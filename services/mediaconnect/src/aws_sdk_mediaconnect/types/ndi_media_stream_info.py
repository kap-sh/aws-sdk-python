"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiMediaStreamInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.frame_resolution
    import aws_sdk_mediaconnect.types.scan_mode


class NdiMediaStreamInfo(TypedDict, closed=True):
    stream_type: NotRequired["str"]
    """<p> The type of media stream (for example, <code>Video</code> or <code>Audio</code>). </p>"""
    codec: NotRequired["str"]
    """<p> The codec used for the media stream. For NDI sources, use <code>speed-hq</code>. </p>"""
    stream_id: NotRequired["int"]
    """<p> A unique identifier for the media stream. </p>"""
    scan_mode: NotRequired["aws_sdk_mediaconnect.types.scan_mode.ScanMode"]
    """<p> The method used to display video frames. Used when the <code>streamType</code> is <code>Video</code>.</p>"""
    frame_resolution: NotRequired[
        "aws_sdk_mediaconnect.types.frame_resolution.FrameResolution"
    ]
    """<p> The width and height dimensions of the video frame in pixels. Used when the <code>streamType</code> is <code>Video</code>. </p>"""
    frame_rate: NotRequired["str"]
    """<p> The number of video frames displayed per second. Used when the <code>streamType</code> is <code>Video</code>. </p>"""
    channels: NotRequired["int"]
    """<p> The number of audio channels in the stream. Used when the <code>streamType</code> is <code>Audio</code>.</p>"""
    sample_rate: NotRequired["int"]
    """<p> The number of audio samples captured per second, measured in kilohertz (kHz). Used when the <code>streamType</code> is <code>Audio</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiMediaStreamInfo) -> dict:
    out: dict = {}
    if "stream_type" in value:
        out["streamType"] = value["stream_type"]
    if "codec" in value:
        out["codec"] = value["codec"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "scan_mode" in value:
        import aws_sdk_mediaconnect.types.scan_mode

        out["scanMode"] = aws_sdk_mediaconnect.types.scan_mode.serialize_json(
            value["scan_mode"]
        )
    if "frame_resolution" in value:
        import aws_sdk_mediaconnect.types.frame_resolution

        out["frameResolution"] = (
            aws_sdk_mediaconnect.types.frame_resolution.serialize_json(
                value["frame_resolution"]
            )
        )
    if "frame_rate" in value:
        out["frameRate"] = value["frame_rate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> NdiMediaStreamInfo:
    out: NdiMediaStreamInfo = {}  # type: ignore[typeddict-item]
    if "streamType" in data:
        out["stream_type"] = data["streamType"]
    if "codec" in data:
        out["codec"] = data["codec"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "scanMode" in data:
        import aws_sdk_mediaconnect.types.scan_mode

        out["scan_mode"] = aws_sdk_mediaconnect.types.scan_mode.deserialize_json(
            data["scanMode"]
        )
    if "frameResolution" in data:
        import aws_sdk_mediaconnect.types.frame_resolution

        out["frame_resolution"] = (
            aws_sdk_mediaconnect.types.frame_resolution.deserialize_json(
                data["frameResolution"]
            )
        )
    if "frameRate" in data:
        out["frame_rate"] = data["frameRate"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
