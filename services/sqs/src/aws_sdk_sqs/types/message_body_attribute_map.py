"""Generated from Smithy shape ``com.amazonaws.sqs#MessageBodyAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.message_attribute_value
    import aws_sdk_sqs.types.string

MessageBodyAttributeMap: TypeAlias = dict[
    "aws_sdk_sqs.types.string.String",
    "aws_sdk_sqs.types.message_attribute_value.MessageAttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MessageBodyAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sqs.types.message_attribute_value

        out[key] = aws_sdk_sqs.types.message_attribute_value.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageBodyAttributeMap:
    out: MessageBodyAttributeMap = {}
    for key, value in data.items():
        import aws_sdk_sqs.types.message_attribute_value

        out[key] = aws_sdk_sqs.types.message_attribute_value.deserialize_aws_json_1_0(
            value
        )
    return out
