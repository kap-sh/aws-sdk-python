"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_association

PhoneNumberAssociationList: TypeAlias = list[
    "capo_chime_sdk_voice.types.phone_number_association.PhoneNumberAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberAssociationList) -> list:
    import capo_chime_sdk_voice.types.phone_number_association

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.phone_number_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PhoneNumberAssociationList:
    import capo_chime_sdk_voice.types.phone_number_association

    out: PhoneNumberAssociationList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.phone_number_association.deserialize_json(item)
        )
    return out
