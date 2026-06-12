"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_update_partition_failure_entry

BatchUpdatePartitionFailureList: TypeAlias = list[
    "aws_sdk_glue.types.batch_update_partition_failure_entry.BatchUpdatePartitionFailureEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionFailureList) -> list:
    import aws_sdk_glue.types.batch_update_partition_failure_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_update_partition_failure_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchUpdatePartitionFailureList:
    import aws_sdk_glue.types.batch_update_partition_failure_entry

    out: BatchUpdatePartitionFailureList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_update_partition_failure_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
