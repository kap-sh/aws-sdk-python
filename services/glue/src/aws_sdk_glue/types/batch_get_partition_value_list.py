"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetPartitionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_value_list

BatchGetPartitionValueList: TypeAlias = list[
    "aws_sdk_glue.types.partition_value_list.PartitionValueList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPartitionValueList) -> list:
    import aws_sdk_glue.types.partition_value_list

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.partition_value_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetPartitionValueList:
    import aws_sdk_glue.types.partition_value_list

    out: BatchGetPartitionValueList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.partition_value_list.deserialize_aws_json_1_1(item)
        )
    return out
