"""Generated from Smithy shape ``com.amazonaws.cloudhsm#PartitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm.types.partition_arn

PartitionList: TypeAlias = list["capo_cloudhsm.types.partition_arn.PartitionArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PartitionList:
    return list(data)
