"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

SipMediaApplicationEndpointList: TypeAlias = list[
    "capo_chime_sdk_voice.types.sip_media_application_endpoint.SipMediaApplicationEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationEndpointList) -> list:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.sip_media_application_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SipMediaApplicationEndpointList:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint

    out: SipMediaApplicationEndpointList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.sip_media_application_endpoint.deserialize_json(
                item
            )
        )
    return out
