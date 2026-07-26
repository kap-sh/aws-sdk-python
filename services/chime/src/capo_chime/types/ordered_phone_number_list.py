"""Generated from Smithy shape ``com.amazonaws.chime#OrderedPhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.ordered_phone_number

OrderedPhoneNumberList: TypeAlias = list[
    "capo_chime.types.ordered_phone_number.OrderedPhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderedPhoneNumberList) -> list:
    import capo_chime.types.ordered_phone_number

    out: list = []
    for item in value:
        out.append(capo_chime.types.ordered_phone_number.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderedPhoneNumberList:
    import capo_chime.types.ordered_phone_number

    out: OrderedPhoneNumberList = []
    for item in data:
        out.append(capo_chime.types.ordered_phone_number.deserialize_json(item))
    return out
