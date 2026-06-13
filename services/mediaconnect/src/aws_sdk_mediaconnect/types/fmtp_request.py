"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FmtpRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.colorimetry
    import aws_sdk_mediaconnect.types.range
    import aws_sdk_mediaconnect.types.scan_mode
    import aws_sdk_mediaconnect.types.tcs


class FmtpRequest(TypedDict):
    channel_order: NotRequired["str"]
    """<p> The format of the audio channel.</p>"""
    colorimetry: NotRequired["aws_sdk_mediaconnect.types.colorimetry.Colorimetry"]
    """<p> The format that is used for the representation of color.</p>"""
    exact_framerate: NotRequired["str"]
    """<p> The frame rate for the video stream, in frames/second. For example: 60000/1001. If you specify a whole number, MediaConnect uses a ratio of N/1. For example, if you specify 60, MediaConnect uses 60/1 as the <code>exactFramerate</code>.</p>"""
    par: NotRequired["str"]
    """<p> The pixel aspect ratio (PAR) of the video.</p>"""
    range: NotRequired["aws_sdk_mediaconnect.types.range.Range"]
    """<p> The encoding range of the video.</p>"""
    scan_mode: NotRequired["aws_sdk_mediaconnect.types.scan_mode.ScanMode"]
    """<p> The type of compression that was used to smooth the video’s appearance.</p>"""
    tcs: NotRequired["aws_sdk_mediaconnect.types.tcs.Tcs"]
    """<p> The transfer characteristic system (TCS) that is used in the video.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FmtpRequest) -> dict:
    out: dict = {}
    if "channel_order" in value:
        out["channelOrder"] = value["channel_order"]
    if "colorimetry" in value:
        import aws_sdk_mediaconnect.types.colorimetry

        out["colorimetry"] = aws_sdk_mediaconnect.types.colorimetry.serialize_json(
            value["colorimetry"]
        )
    if "exact_framerate" in value:
        out["exactFramerate"] = value["exact_framerate"]
    if "par" in value:
        out["par"] = value["par"]
    if "range" in value:
        import aws_sdk_mediaconnect.types.range

        out["range"] = aws_sdk_mediaconnect.types.range.serialize_json(value["range"])
    if "scan_mode" in value:
        import aws_sdk_mediaconnect.types.scan_mode

        out["scanMode"] = aws_sdk_mediaconnect.types.scan_mode.serialize_json(
            value["scan_mode"]
        )
    if "tcs" in value:
        import aws_sdk_mediaconnect.types.tcs

        out["tcs"] = aws_sdk_mediaconnect.types.tcs.serialize_json(value["tcs"])
    return out


def deserialize_json(data: dict) -> FmtpRequest:
    out: FmtpRequest = {}  # type: ignore[typeddict-item]
    if "channelOrder" in data:
        out["channel_order"] = data["channelOrder"]
    if "colorimetry" in data:
        import aws_sdk_mediaconnect.types.colorimetry

        out["colorimetry"] = aws_sdk_mediaconnect.types.colorimetry.deserialize_json(
            data["colorimetry"]
        )
    if "exactFramerate" in data:
        out["exact_framerate"] = data["exactFramerate"]
    if "par" in data:
        out["par"] = data["par"]
    if "range" in data:
        import aws_sdk_mediaconnect.types.range

        out["range"] = aws_sdk_mediaconnect.types.range.deserialize_json(data["range"])
    if "scanMode" in data:
        import aws_sdk_mediaconnect.types.scan_mode

        out["scan_mode"] = aws_sdk_mediaconnect.types.scan_mode.deserialize_json(
            data["scanMode"]
        )
    if "tcs" in data:
        import aws_sdk_mediaconnect.types.tcs

        out["tcs"] = aws_sdk_mediaconnect.types.tcs.deserialize_json(data["tcs"])
    return out
