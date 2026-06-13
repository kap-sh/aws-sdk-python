"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.fmtp_request


class MediaStreamAttributesRequest(TypedDict):
    fmtp: NotRequired["aws_sdk_mediaconnect.types.fmtp_request.FmtpRequest"]
    """<p>The settings that you want to use to define the media stream. </p>"""
    lang: NotRequired["str"]
    """<p>The audio language, in a format that is recognized by the receiver. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamAttributesRequest) -> dict:
    out: dict = {}
    if "fmtp" in value:
        import aws_sdk_mediaconnect.types.fmtp_request

        out["fmtp"] = aws_sdk_mediaconnect.types.fmtp_request.serialize_json(
            value["fmtp"]
        )
    if "lang" in value:
        out["lang"] = value["lang"]
    return out


def deserialize_json(data: dict) -> MediaStreamAttributesRequest:
    out: MediaStreamAttributesRequest = {}  # type: ignore[typeddict-item]
    if "fmtp" in data:
        import aws_sdk_mediaconnect.types.fmtp_request

        out["fmtp"] = aws_sdk_mediaconnect.types.fmtp_request.deserialize_json(
            data["fmtp"]
        )
    if "lang" in data:
        out["lang"] = data["lang"]
    return out
