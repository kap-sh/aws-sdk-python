"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update

ReplicaGlobalSecondaryIndexAutoScalingUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_update.ReplicaGlobalSecondaryIndexAutoScalingUpdate"
]
