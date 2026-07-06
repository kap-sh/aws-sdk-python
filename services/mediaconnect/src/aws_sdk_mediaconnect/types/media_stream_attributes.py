"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.fmtp


class MediaStreamAttributes(TypedDict, closed=True):
    fmtp: NotRequired["aws_sdk_mediaconnect.types.fmtp.Fmtp"]
    """<p>The settings that you want to use to define the media stream. </p>"""
    lang: NotRequired["str"]
    """<p>The audio language, in a format that is recognized by the receiver. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamAttributes) -> dict:
    out: dict = {}
    if "fmtp" in value:
        import aws_sdk_mediaconnect.types.fmtp

        out["fmtp"] = aws_sdk_mediaconnect.types.fmtp.serialize_json(value["fmtp"])
    if "lang" in value:
        out["lang"] = value["lang"]
    return out


def deserialize_json(data: dict) -> MediaStreamAttributes:
    out: MediaStreamAttributes = {}  # type: ignore[typeddict-item]
    if "fmtp" in data:
        import aws_sdk_mediaconnect.types.fmtp

        out["fmtp"] = aws_sdk_mediaconnect.types.fmtp.deserialize_json(data["fmtp"])
    if "lang" in data:
        out["lang"] = data["lang"]
    return out
