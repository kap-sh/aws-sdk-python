"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.message_system_attribute_name

MessageSystemAttributeList: TypeAlias = list[
    "capo_sqs.types.message_system_attribute_name.MessageSystemAttributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageSystemAttributeList) -> list:
    import capo_sqs.types.message_system_attribute_name

    out: list = []
    for item in value:
        out.append(
            capo_sqs.types.message_system_attribute_name.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MessageSystemAttributeList:
    import capo_sqs.types.message_system_attribute_name

    out: MessageSystemAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sqs.types.message_system_attribute_name.deserialize_aws_json_1_0(item)
        )
    return out
