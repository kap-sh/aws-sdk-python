"""Generated from Smithy shape ``com.amazonaws.sqs#MessageBodySystemAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.message_system_attribute_name_for_sends
    import capo_sqs.types.message_system_attribute_value

MessageBodySystemAttributeMap: TypeAlias = dict[
    "capo_sqs.types.message_system_attribute_name_for_sends.MessageSystemAttributeNameForSends",
    "capo_sqs.types.message_system_attribute_value.MessageSystemAttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MessageBodySystemAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sqs.types.message_system_attribute_name_for_sends
        import capo_sqs.types.message_system_attribute_value

        out[
            capo_sqs.types.message_system_attribute_name_for_sends.serialize_aws_json_1_0(
                key
            )
        ] = capo_sqs.types.message_system_attribute_value.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageBodySystemAttributeMap:
    out: MessageBodySystemAttributeMap = {}
    for key, value in data.items():
        import capo_sqs.types.message_system_attribute_name_for_sends
        import capo_sqs.types.message_system_attribute_value

        out[
            capo_sqs.types.message_system_attribute_name_for_sends.deserialize_aws_json_1_0(
                key
            )
        ] = capo_sqs.types.message_system_attribute_value.deserialize_aws_json_1_0(
            value
        )
    return out
