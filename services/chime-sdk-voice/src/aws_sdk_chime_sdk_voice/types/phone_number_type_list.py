"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.phone_number_type

PhoneNumberTypeList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.phone_number_type.PhoneNumberType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberTypeList) -> list:
    import aws_sdk_chime_sdk_voice.types.phone_number_type

    out: list = []
    for item in value:
        out.append(aws_sdk_chime_sdk_voice.types.phone_number_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberTypeList:
    import aws_sdk_chime_sdk_voice.types.phone_number_type

    out: PhoneNumberTypeList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.phone_number_type.deserialize_json(item)
        )
    return out
