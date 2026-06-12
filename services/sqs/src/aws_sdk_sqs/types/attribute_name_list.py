"""Generated from Smithy shape ``com.amazonaws.sqs#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.queue_attribute_name

AttributeNameList: TypeAlias = list[
    "aws_sdk_sqs.types.queue_attribute_name.QueueAttributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeNameList) -> list:
    import aws_sdk_sqs.types.queue_attribute_name

    out: list = []
    for item in value:
        out.append(aws_sdk_sqs.types.queue_attribute_name.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AttributeNameList:
    import aws_sdk_sqs.types.queue_attribute_name

    out: AttributeNameList = []
    for item in data:
        out.append(
            aws_sdk_sqs.types.queue_attribute_name.deserialize_aws_json_1_0(item)
        )
    return out
