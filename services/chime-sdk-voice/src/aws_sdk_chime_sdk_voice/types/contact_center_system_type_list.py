"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ContactCenterSystemTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.contact_center_system_type

ContactCenterSystemTypeList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.contact_center_system_type.ContactCenterSystemType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactCenterSystemTypeList) -> list:
    import aws_sdk_chime_sdk_voice.types.contact_center_system_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.contact_center_system_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContactCenterSystemTypeList:
    import aws_sdk_chime_sdk_voice.types.contact_center_system_type

    out: ContactCenterSystemTypeList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.contact_center_system_type.deserialize_json(
                item
            )
        )
    return out
