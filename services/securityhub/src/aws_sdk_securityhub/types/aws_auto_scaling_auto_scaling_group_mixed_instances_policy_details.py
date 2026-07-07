"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details
    import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails(TypedDict, closed=True):
    instances_distribution: NotRequired[
        "aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails"
    ]
    """<p>The instances distribution. The instances distribution specifies the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacity.</p>"""
    launch_template: NotRequired[
        "aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails"
    ]
    """<p>The launch template to use and the instance types (overrides) to use to provision EC2 instances to fulfill On-Demand and Spot capacities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails,
) -> dict:
    out: dict = {}
    if "instances_distribution" in value:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details

        out["InstancesDistribution"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details.serialize_json(
                value["instances_distribution"]
            )
        )
    if "launch_template" in value:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details

        out["LaunchTemplate"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details.serialize_json(
                value["launch_template"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails:
    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails = {}  # type: ignore[typeddict-item]
    if "InstancesDistribution" in data:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details

        out["instances_distribution"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_instances_distribution_details.deserialize_json(
                data["InstancesDistribution"]
            )
        )
    if "LaunchTemplate" in data:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details

        out["launch_template"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_details.deserialize_json(
                data["LaunchTemplate"]
            )
        )
    return out
