"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application


class CreateSipMediaApplicationResponse(TypedDict, closed=True):
    sip_media_application: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application.SipMediaApplication"
    ]
    """<p>The SIP media application details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationResponse) -> dict:
    out: dict = {}
    if "sip_media_application" in value:
        import capo_chime_sdk_voice.types.sip_media_application

        out["SipMediaApplication"] = (
            capo_chime_sdk_voice.types.sip_media_application.serialize_json(
                value["sip_media_application"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationResponse:
    out: CreateSipMediaApplicationResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplication" in data:
        import capo_chime_sdk_voice.types.sip_media_application

        out["sip_media_application"] = (
            capo_chime_sdk_voice.types.sip_media_application.deserialize_json(
                data["SipMediaApplication"]
            )
        )
    return out
