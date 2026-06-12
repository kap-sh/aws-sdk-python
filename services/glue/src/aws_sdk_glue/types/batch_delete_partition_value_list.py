"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeletePartitionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_value_list

BatchDeletePartitionValueList: TypeAlias = list[
    "aws_sdk_glue.types.partition_value_list.PartitionValueList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeletePartitionValueList) -> list:
    import aws_sdk_glue.types.partition_value_list

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.partition_value_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeletePartitionValueList:
    import aws_sdk_glue.types.partition_value_list

    out: BatchDeletePartitionValueList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.partition_value_list.deserialize_aws_json_1_1(item)
        )
    return out
