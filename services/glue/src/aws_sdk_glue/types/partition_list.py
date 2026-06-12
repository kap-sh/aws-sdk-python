"""Generated from Smithy shape ``com.amazonaws.glue#PartitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition

PartitionList: TypeAlias = list["aws_sdk_glue.types.partition.Partition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionList) -> list:
    import aws_sdk_glue.types.partition

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.partition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionList:
    import aws_sdk_glue.types.partition

    out: PartitionList = []
    for item in data:
        out.append(aws_sdk_glue.types.partition.deserialize_aws_json_1_1(item))
    return out
