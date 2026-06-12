"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.partition_key

PartitionKeyList: TypeAlias = list[
    "aws_sdk_timestream_write.types.partition_key.PartitionKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartitionKeyList) -> list:
    import aws_sdk_timestream_write.types.partition_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_write.types.partition_key.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartitionKeyList:
    import aws_sdk_timestream_write.types.partition_key

    out: PartitionKeyList = []
    for item in data:
        out.append(
            aws_sdk_timestream_write.types.partition_key.deserialize_aws_json_1_0(item)
        )
    return out
