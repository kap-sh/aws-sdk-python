"""Generated from Smithy shape ``com.amazonaws.osis#ValidationMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.validation_message

ValidationMessageList: TypeAlias = list[
    "aws_sdk_osis.types.validation_message.ValidationMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMessageList) -> list:
    import aws_sdk_osis.types.validation_message

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.validation_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationMessageList:
    import aws_sdk_osis.types.validation_message

    out: ValidationMessageList = []
    for item in data:
        out.append(aws_sdk_osis.types.validation_message.deserialize_json(item))
    return out
