"""Generated from Smithy shape ``com.amazonaws.timestreamquery#PartitionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.partition_key

PartitionKeyList: TypeAlias = list[
    "aws_sdk_timestream_query.types.partition_key.PartitionKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PartitionKeyList:
    return list(data)
