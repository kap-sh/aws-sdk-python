"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_error

PhoneNumberErrorList: TypeAlias = list[
    "aws_sdk_chime.types.phone_number_error.PhoneNumberError"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberErrorList) -> list:
    import aws_sdk_chime.types.phone_number_error

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.phone_number_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberErrorList:
    import aws_sdk_chime.types.phone_number_error

    out: PhoneNumberErrorList = []
    for item in data:
        out.append(aws_sdk_chime.types.phone_number_error.deserialize_json(item))
    return out
