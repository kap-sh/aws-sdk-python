"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_update

ReplicaUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_update.ReplicaUpdate"
]
