"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicationGroupUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replication_group_update

ReplicationGroupUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replication_group_update.ReplicationGroupUpdate"
]
