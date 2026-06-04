"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicationGroupUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replication_group_update

ReplicationGroupUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replication_group_update.ReplicationGroupUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupUpdateList) -> list:
    import aws_sdk_dynamodb.types.replication_group_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.replication_group_update.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReplicationGroupUpdateList:
    import aws_sdk_dynamodb.types.replication_group_update

    out: ReplicationGroupUpdateList = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.replication_group_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
