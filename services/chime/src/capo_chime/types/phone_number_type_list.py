"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.phone_number_type

PhoneNumberTypeList: TypeAlias = list[
    "capo_chime.types.phone_number_type.PhoneNumberType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberTypeList) -> list:
    import capo_chime.types.phone_number_type

    out: list = []
    for item in value:
        out.append(capo_chime.types.phone_number_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberTypeList:
    import capo_chime.types.phone_number_type

    out: PhoneNumberTypeList = []
    for item in data:
        out.append(capo_chime.types.phone_number_type.deserialize_json(item))
    return out
