"""Generated from Smithy shape ``com.amazonaws.glue#PartitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.partition

PartitionList: TypeAlias = list["capo_glue.types.partition.Partition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionList) -> list:
    import capo_glue.types.partition

    out: list = []
    for item in value:
        out.append(capo_glue.types.partition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionList:
    import capo_glue.types.partition

    out: PartitionList = []
    for item in data:
        out.append(capo_glue.types.partition.deserialize_aws_json_1_1(item))
    return out
