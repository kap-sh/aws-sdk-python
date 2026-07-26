"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application

SipMediaApplicationList: TypeAlias = list[
    "capo_chime_sdk_voice.types.sip_media_application.SipMediaApplication"
]


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationList) -> list:
    import capo_chime_sdk_voice.types.sip_media_application

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.sip_media_application.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SipMediaApplicationList:
    import capo_chime_sdk_voice.types.sip_media_application

    out: SipMediaApplicationList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.sip_media_application.deserialize_json(item)
        )
    return out
