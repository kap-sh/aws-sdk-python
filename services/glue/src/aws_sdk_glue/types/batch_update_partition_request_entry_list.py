"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_update_partition_request_entry

BatchUpdatePartitionRequestEntryList: TypeAlias = list[
    "aws_sdk_glue.types.batch_update_partition_request_entry.BatchUpdatePartitionRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionRequestEntryList) -> list:
    import aws_sdk_glue.types.batch_update_partition_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_update_partition_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchUpdatePartitionRequestEntryList:
    import aws_sdk_glue.types.batch_update_partition_request_entry

    out: BatchUpdatePartitionRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_update_partition_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
