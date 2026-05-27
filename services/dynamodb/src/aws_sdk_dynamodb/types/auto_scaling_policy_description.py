"""Generated from Smithy shape ``com.amazonaws.dynamodb#AutoScalingPolicyDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.auto_scaling_policy_name
    import aws_sdk_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description


class AutoScalingPolicyDescription(TypedDict):
    policy_name: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_policy_name.AutoScalingPolicyName"
    ]
    """<p>The name of the scaling policy.</p>"""
    target_tracking_scaling_policy_configuration: NotRequired[
        "aws_sdk_dynamodb.types.auto_scaling_target_tracking_scaling_policy_configuration_description.AutoScalingTargetTrackingScalingPolicyConfigurationDescription"
    ]
    """<p>Represents a target tracking scaling policy configuration.</p>"""
