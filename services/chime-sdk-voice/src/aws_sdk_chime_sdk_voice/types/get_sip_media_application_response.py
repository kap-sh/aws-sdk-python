"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipMediaApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application


class GetSipMediaApplicationResponse(TypedDict, closed=True):
    sip_media_application: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application.SipMediaApplication"
    ]
    """<p>The details of the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipMediaApplicationResponse) -> dict:
    out: dict = {}
    if "sip_media_application" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application

        out["SipMediaApplication"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application.serialize_json(
                value["sip_media_application"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSipMediaApplicationResponse:
    out: GetSipMediaApplicationResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplication" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application

        out["sip_media_application"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application.deserialize_json(
                data["SipMediaApplication"]
            )
        )
    return out
