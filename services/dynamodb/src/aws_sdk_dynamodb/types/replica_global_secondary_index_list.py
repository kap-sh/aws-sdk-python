"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index

ReplicaGlobalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index.ReplicaGlobalSecondaryIndex"
]
