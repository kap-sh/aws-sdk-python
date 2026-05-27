"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_policy_name
    import aws_sdk_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update


class AutoScalingPolicyUpdate(TypedDict):
    policy_name: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_policy_name.AutoScalingPolicyName"
    ]
    """<p>The name of the scaling policy.</p>"""
    target_tracking_scaling_policy_configuration: "aws_sdk_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_update.AutoScalingTargetTrackingScalingPolicyConfigurationUpdate"
    """<p>Represents a target tracking scaling policy configuration.</p>"""
