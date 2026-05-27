"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAutoScalingDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_auto_scaling_description

ReplicaAutoScalingDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.replica_auto_scaling_description.ReplicaAutoScalingDescription"
]
