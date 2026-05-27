"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaGlobalSecondaryIndexAutoScalingDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description

ReplicaGlobalSecondaryIndexAutoScalingDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_global_secondary_index_auto_scaling_description.ReplicaGlobalSecondaryIndexAutoScalingDescription"
]
