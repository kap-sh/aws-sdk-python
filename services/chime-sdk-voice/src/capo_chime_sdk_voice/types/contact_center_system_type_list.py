"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ContactCenterSystemTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.contact_center_system_type

ContactCenterSystemTypeList: TypeAlias = list[
    "capo_chime_sdk_voice.types.contact_center_system_type.ContactCenterSystemType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactCenterSystemTypeList) -> list:
    import capo_chime_sdk_voice.types.contact_center_system_type

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.contact_center_system_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactCenterSystemTypeList:
    import capo_chime_sdk_voice.types.contact_center_system_type

    out: ContactCenterSystemTypeList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.contact_center_system_type.deserialize_json(item)
        )
    return out
