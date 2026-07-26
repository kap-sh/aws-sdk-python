"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.message_system_attribute_name
    import capo_sqs.types.string

MessageSystemAttributeMap: TypeAlias = dict[
    "capo_sqs.types.message_system_attribute_name.MessageSystemAttributeName",
    "capo_sqs.types.string.String",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: MessageSystemAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sqs.types.message_system_attribute_name

        out[
            capo_sqs.types.message_system_attribute_name.serialize_aws_json_1_0(key)
        ] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageSystemAttributeMap:
    out: MessageSystemAttributeMap = {}
    for key, value in data.items():
        import capo_sqs.types.message_system_attribute_name

        out[
            capo_sqs.types.message_system_attribute_name.deserialize_aws_json_1_0(key)
        ] = value
    return out
