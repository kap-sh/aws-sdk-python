"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberOrderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_order

PhoneNumberOrderList: TypeAlias = list[
    "aws_sdk_chime.types.phone_number_order.PhoneNumberOrder"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberOrderList) -> list:
    import aws_sdk_chime.types.phone_number_order

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.phone_number_order.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberOrderList:
    import aws_sdk_chime.types.phone_number_order

    out: PhoneNumberOrderList = []
    for item in data:
        out.append(aws_sdk_chime.types.phone_number_order.deserialize_json(item))
    return out
