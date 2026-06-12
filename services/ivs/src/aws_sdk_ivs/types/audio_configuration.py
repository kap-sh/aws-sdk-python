"""Generated from Smithy shape ``com.amazonaws.ivs#AudioConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.integer
    import aws_sdk_ivs.types.string


class AudioConfiguration(TypedDict):
    codec: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>Codec used for the audio encoding.</p>"""
    target_bitrate: "aws_sdk_ivs.types.integer.Integer"
    """<p>The expected ingest bitrate (bits per second). This is configured in the encoder.</p>"""
    sample_rate: "aws_sdk_ivs.types.integer.Integer"
    """<p>Number of audio samples recorded per second.</p>"""
    channels: "aws_sdk_ivs.types.integer.Integer"
    """<p>Number of audio channels.</p>"""
    track: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>Name of the audio track (if the stream has an audio track). If multitrack is not enabled, this is Track0 (the sole track).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioConfiguration) -> dict:
    out: dict = {}
    if "codec" in value:
        out["codec"] = value["codec"]
    out["targetBitrate"] = value.get("target_bitrate", 0)
    out["sampleRate"] = value.get("sample_rate", 0)
    out["channels"] = value.get("channels", 0)
    if "track" in value:
        out["track"] = value["track"]
    return out


def deserialize_json(data: dict) -> AudioConfiguration:
    out: AudioConfiguration = {}  # type: ignore[typeddict-item]
    if "codec" in data:
        out["codec"] = data["codec"]
    if "targetBitrate" in data:
        out["target_bitrate"] = data["targetBitrate"]
    else:
        out["target_bitrate"] = 0
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    else:
        out["sample_rate"] = 0
    if "channels" in data:
        out["channels"] = data["channels"]
    else:
        out["channels"] = 0
    if "track" in data:
        out["track"] = data["track"]
    return out
