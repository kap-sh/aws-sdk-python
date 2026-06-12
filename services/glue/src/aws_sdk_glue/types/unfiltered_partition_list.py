"""Generated from Smithy shape ``com.amazonaws.glue#UnfilteredPartitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.unfiltered_partition

UnfilteredPartitionList: TypeAlias = list[
    "aws_sdk_glue.types.unfiltered_partition.UnfilteredPartition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnfilteredPartitionList) -> list:
    import aws_sdk_glue.types.unfiltered_partition

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.unfiltered_partition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnfilteredPartitionList:
    import aws_sdk_glue.types.unfiltered_partition

    out: UnfilteredPartitionList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.unfiltered_partition.deserialize_aws_json_1_1(item)
        )
    return out
