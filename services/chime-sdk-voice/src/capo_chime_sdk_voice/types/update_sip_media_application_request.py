"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list
    import capo_chime_sdk_voice.types.sip_media_application_name


class UpdateSipMediaApplicationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""
    name: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    ]
    """<p>The new name for the specified SIP media application.</p>"""
    endpoints: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    ]
    """<p>The new set of endpoints for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSipMediaApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["Endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
                value["endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSipMediaApplicationRequest:
    out: UpdateSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Endpoints" in data:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    return out
