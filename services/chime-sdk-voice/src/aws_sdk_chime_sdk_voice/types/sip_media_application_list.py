"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application

SipMediaApplicationList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.sip_media_application.SipMediaApplication"
]


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationList) -> list:
    import aws_sdk_chime_sdk_voice.types.sip_media_application

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.sip_media_application.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SipMediaApplicationList:
    import aws_sdk_chime_sdk_voice.types.sip_media_application

    out: SipMediaApplicationList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.sip_media_application.deserialize_json(item)
        )
    return out
