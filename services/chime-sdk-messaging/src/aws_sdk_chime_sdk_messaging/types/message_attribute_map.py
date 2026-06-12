"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessageAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.message_attribute_name
    import aws_sdk_chime_sdk_messaging.types.message_attribute_value

MessageAttributeMap: TypeAlias = dict[
    "aws_sdk_chime_sdk_messaging.types.message_attribute_name.MessageAttributeName",
    "aws_sdk_chime_sdk_messaging.types.message_attribute_value.MessageAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MessageAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_chime_sdk_messaging.types.message_attribute_value

        out[key] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> MessageAttributeMap:
    out: MessageAttributeMap = {}
    for key, value in data.items():
        import aws_sdk_chime_sdk_messaging.types.message_attribute_value

        out[key] = (
            aws_sdk_chime_sdk_messaging.types.message_attribute_value.deserialize_json(
                value
            )
        )
    return out
