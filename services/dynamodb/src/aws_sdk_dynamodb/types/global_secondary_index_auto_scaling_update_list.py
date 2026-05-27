"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexAutoScalingUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update

GlobalSecondaryIndexAutoScalingUpdateList: TypeAlias = list[
    "aws_sdk_dynamodb.types.global_secondary_index_auto_scaling_update.GlobalSecondaryIndexAutoScalingUpdate"
]
