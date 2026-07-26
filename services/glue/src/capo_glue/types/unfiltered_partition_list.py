"""Generated from Smithy shape ``com.amazonaws.glue#UnfilteredPartitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.unfiltered_partition

UnfilteredPartitionList: TypeAlias = list[
    "capo_glue.types.unfiltered_partition.UnfilteredPartition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnfilteredPartitionList) -> list:
    import capo_glue.types.unfiltered_partition

    out: list = []
    for item in value:
        out.append(capo_glue.types.unfiltered_partition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnfilteredPartitionList:
    import capo_glue.types.unfiltered_partition

    out: UnfilteredPartitionList = []
    for item in data:
        out.append(capo_glue.types.unfiltered_partition.deserialize_aws_json_1_1(item))
    return out
