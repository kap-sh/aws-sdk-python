"""Generated from Smithy shape ``com.amazonaws.ivs#VideoConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.integer
    import capo_ivs.types.string


class VideoConfiguration(TypedDict, closed=True):
    avc_profile: NotRequired["capo_ivs.types.string.String"]
    """<p>(Deprecated) Indicates to the decoder the requirements for decoding the stream. For definitions of the valid values, see the H.264 specification. This is populated only when VideoConfiguration is part of the deprecated IngestConfiguration; otherwise, this is an empty string.</p>"""
    avc_level: NotRequired["capo_ivs.types.string.String"]
    """<p>(Deprecated) Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. For details, see the H.264 specification. This is populated only when VideoConfiguration is part of the deprecated IngestConfiguration; otherwise, this is an empty string.</p>"""
    codec: NotRequired["capo_ivs.types.string.String"]
    """<p>Codec used for the video encoding.</p>"""
    encoder: NotRequired["capo_ivs.types.string.String"]
    """<p>Software or hardware used to encode the video.</p>"""
    target_bitrate: "capo_ivs.types.integer.Integer"
    """<p>The expected ingest bitrate (bits per second). This is configured in the encoder.</p>"""
    target_framerate: "capo_ivs.types.integer.Integer"
    """<p>The expected ingest framerate. This is configured in the encoder.</p>"""
    video_height: "capo_ivs.types.integer.Integer"
    """<p>Video-resolution height in pixels.</p>"""
    video_width: "capo_ivs.types.integer.Integer"
    """<p>Video-resolution width in pixels.</p>"""
    level: NotRequired["capo_ivs.types.string.String"]
    """<p>Indicates the degree of required decoder performance for a profile. Normally this is set automatically by the encoder. When an AVC codec is used, this field has the same value as <code>avcLevel</code>.</p>"""
    track: NotRequired["capo_ivs.types.string.String"]
    """<p>Name of the video track. If multitrack is not enabled, this is Track0 (the sole track).</p>"""
    profile: NotRequired["capo_ivs.types.string.String"]
    """<p>Indicates to the decoder the requirements for decoding the stream. When an AVC codec is used, this field has the same value as <code>avcProfile</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoConfiguration) -> dict:
    out: dict = {}
    if "avc_profile" in value:
        out["avcProfile"] = value["avc_profile"]
    if "avc_level" in value:
        out["avcLevel"] = value["avc_level"]
    if "codec" in value:
        out["codec"] = value["codec"]
    if "encoder" in value:
        out["encoder"] = value["encoder"]
    out["targetBitrate"] = value.get("target_bitrate", 0)
    out["targetFramerate"] = value.get("target_framerate", 0)
    out["videoHeight"] = value.get("video_height", 0)
    out["videoWidth"] = value.get("video_width", 0)
    if "level" in value:
        out["level"] = value["level"]
    if "track" in value:
        out["track"] = value["track"]
    if "profile" in value:
        out["profile"] = value["profile"]
    return out


def deserialize_json(data: dict) -> VideoConfiguration:
    out: VideoConfiguration = {}  # type: ignore[typeddict-item]
    if "avcProfile" in data:
        out["avc_profile"] = data["avcProfile"]
    if "avcLevel" in data:
        out["avc_level"] = data["avcLevel"]
    if "codec" in data:
        out["codec"] = data["codec"]
    if "encoder" in data:
        out["encoder"] = data["encoder"]
    if "targetBitrate" in data:
        out["target_bitrate"] = data["targetBitrate"]
    else:
        out["target_bitrate"] = 0
    if "targetFramerate" in data:
        out["target_framerate"] = data["targetFramerate"]
    else:
        out["target_framerate"] = 0
    if "videoHeight" in data:
        out["video_height"] = data["videoHeight"]
    else:
        out["video_height"] = 0
    if "videoWidth" in data:
        out["video_width"] = data["videoWidth"]
    else:
        out["video_width"] = 0
    if "level" in data:
        out["level"] = data["level"]
    if "track" in data:
        out["track"] = data["track"]
    if "profile" in data:
        out["profile"] = data["profile"]
    return out
