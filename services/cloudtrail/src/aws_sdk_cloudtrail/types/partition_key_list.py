"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PartitionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.partition_key

PartitionKeyList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.partition_key.PartitionKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionKeyList) -> list:
    import aws_sdk_cloudtrail.types.partition_key

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.partition_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionKeyList:
    import aws_sdk_cloudtrail.types.partition_key

    out: PartitionKeyList = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.partition_key.deserialize_aws_json_1_1(item)
        )
    return out
