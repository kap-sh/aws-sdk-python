"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationCallResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application_call


class CreateSipMediaApplicationCallResponse(TypedDict):
    sip_media_application_call: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_call.SipMediaApplicationCall"
    ]
    """<p>The actual call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationCallResponse) -> dict:
    out: dict = {}
    if "sip_media_application_call" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_call

        out["SipMediaApplicationCall"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_call.serialize_json(
                value["sip_media_application_call"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationCallResponse:
    out: CreateSipMediaApplicationCallResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationCall" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_call

        out["sip_media_application_call"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_call.deserialize_json(
                data["SipMediaApplicationCall"]
            )
        )
    return out
