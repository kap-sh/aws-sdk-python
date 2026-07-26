"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.phone_number_type

PhoneNumberTypes: TypeAlias = list[
    "capo_connect.types.phone_number_type.PhoneNumberType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberTypes) -> list:
    import capo_connect.types.phone_number_type

    out: list = []
    for item in value:
        out.append(capo_connect.types.phone_number_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberTypes:
    import capo_connect.types.phone_number_type

    out: PhoneNumberTypes = []
    for item in data:
        out.append(capo_connect.types.phone_number_type.deserialize_json(item))
    return out
