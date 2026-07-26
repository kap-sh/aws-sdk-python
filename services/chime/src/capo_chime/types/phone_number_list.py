"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.phone_number

PhoneNumberList: TypeAlias = list["capo_chime.types.phone_number.PhoneNumber"]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberList) -> list:
    import capo_chime.types.phone_number

    out: list = []
    for item in value:
        out.append(capo_chime.types.phone_number.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberList:
    import capo_chime.types.phone_number

    out: PhoneNumberList = []
    for item in data:
        out.append(capo_chime.types.phone_number.deserialize_json(item))
    return out
