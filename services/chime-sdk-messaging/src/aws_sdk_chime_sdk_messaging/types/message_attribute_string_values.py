"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessageAttributeStringValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.message_attribute_string_value

MessageAttributeStringValues: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.message_attribute_string_value.MessageAttributeStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageAttributeStringValues) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageAttributeStringValues:
    return list(data)
