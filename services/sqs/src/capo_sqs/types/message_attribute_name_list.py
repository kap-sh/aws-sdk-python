"""Generated from Smithy shape ``com.amazonaws.sqs#MessageAttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.message_attribute_name

MessageAttributeNameList: TypeAlias = list[
    "capo_sqs.types.message_attribute_name.MessageAttributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageAttributeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> MessageAttributeNameList:
    return [item for item in data if item is not None]
