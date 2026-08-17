"""Generated from Smithy shape ``com.amazonaws.sqs#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.queue_attribute_name

AttributeNameList: TypeAlias = list[
    "capo_sqs.types.queue_attribute_name.QueueAttributeName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeNameList) -> list:
    import capo_sqs.types.queue_attribute_name

    out: list = []
    for item in value:
        out.append(capo_sqs.types.queue_attribute_name.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AttributeNameList:
    import capo_sqs.types.queue_attribute_name

    out: AttributeNameList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sqs.types.queue_attribute_name.deserialize_aws_json_1_0(item))
    return out
