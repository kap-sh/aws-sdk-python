"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_auto_scaling_update

ReplicaAutoScalingUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_auto_scaling_update.ReplicaAutoScalingUpdate"
]
