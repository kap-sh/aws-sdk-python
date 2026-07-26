"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.partition_index

PartitionIndexList: TypeAlias = list["capo_glue.types.partition_index.PartitionIndex"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndexList) -> list:
    import capo_glue.types.partition_index

    out: list = []
    for item in value:
        out.append(capo_glue.types.partition_index.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionIndexList:
    import capo_glue.types.partition_index

    out: PartitionIndexList = []
    for item in data:
        out.append(capo_glue.types.partition_index.deserialize_aws_json_1_1(item))
    return out
