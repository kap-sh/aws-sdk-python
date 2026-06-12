"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OrderedPhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.ordered_phone_number

OrderedPhoneNumberList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.ordered_phone_number.OrderedPhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderedPhoneNumberList) -> list:
    import aws_sdk_chime_sdk_voice.types.ordered_phone_number

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.ordered_phone_number.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrderedPhoneNumberList:
    import aws_sdk_chime_sdk_voice.types.ordered_phone_number

    out: OrderedPhoneNumberList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.ordered_phone_number.deserialize_json(item)
        )
    return out
