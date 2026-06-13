"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportStream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.frame_resolution


class TransportStream(TypedDict):
    channels: NotRequired["int"]
    """<p> The number of channels in the audio stream.</p>"""
    codec: NotRequired["str"]
    """<p> The codec used by the stream.</p>"""
    frame_rate: NotRequired["str"]
    """<p> The frame rate used by the video stream.</p>"""
    frame_resolution: NotRequired[
        "aws_sdk_mediaconnect.types.frame_resolution.FrameResolution"
    ]
    """<p>The frame resolution used by the video stream. </p>"""
    pid: NotRequired["int"]
    """<p> The Packet ID (PID) as it is reported in the Program Map Table.</p>"""
    sample_rate: NotRequired["int"]
    """<p> The sample rate used by the audio stream.</p>"""
    sample_size: NotRequired["int"]
    """<p> The sample bit size used by the audio stream.</p>"""
    stream_type: NotRequired["str"]
    """<p> The Stream Type as it is reported in the Program Map Table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransportStream) -> dict:
    out: dict = {}
    if "channels" in value:
        out["channels"] = value["channels"]
    if "codec" in value:
        out["codec"] = value["codec"]
    if "frame_rate" in value:
        out["frameRate"] = value["frame_rate"]
    if "frame_resolution" in value:
        import aws_sdk_mediaconnect.types.frame_resolution

        out["frameResolution"] = (
            aws_sdk_mediaconnect.types.frame_resolution.serialize_json(
                value["frame_resolution"]
            )
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "sample_size" in value:
        out["sampleSize"] = value["sample_size"]
    if "stream_type" in value:
        out["streamType"] = value["stream_type"]
    return out


def deserialize_json(data: dict) -> TransportStream:
    out: TransportStream = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "codec" in data:
        out["codec"] = data["codec"]
    if "frameRate" in data:
        out["frame_rate"] = data["frameRate"]
    if "frameResolution" in data:
        import aws_sdk_mediaconnect.types.frame_resolution

        out["frame_resolution"] = (
            aws_sdk_mediaconnect.types.frame_resolution.deserialize_json(
                data["frameResolution"]
            )
        )
    if "pid" in data:
        out["pid"] = data["pid"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "sampleSize" in data:
        out["sample_size"] = data["sampleSize"]
    if "streamType" in data:
        out["stream_type"] = data["streamType"]
    return out
