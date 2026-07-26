"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationCallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application_call


class CreateSipMediaApplicationCallResponse(TypedDict, closed=True):
    sip_media_application_call: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_call.SipMediaApplicationCall"
    ]
    """<p>The actual call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationCallResponse) -> dict:
    out: dict = {}
    if "sip_media_application_call" in value:
        import capo_chime_sdk_voice.types.sip_media_application_call

        out["SipMediaApplicationCall"] = (
            capo_chime_sdk_voice.types.sip_media_application_call.serialize_json(
                value["sip_media_application_call"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationCallResponse:
    out: CreateSipMediaApplicationCallResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationCall" in data:
        import capo_chime_sdk_voice.types.sip_media_application_call

        out["sip_media_application_call"] = (
            capo_chime_sdk_voice.types.sip_media_application_call.deserialize_json(
                data["SipMediaApplicationCall"]
            )
        )
    return out
