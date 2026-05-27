"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_policy_description

AutoScalingPolicyDescriptionList: TypeAlias = list[
    "aws_sdk_dynamodb.types.auto_scaling_policy_description.AutoScalingPolicyDescription"
]
