"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list
    import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification
    import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsAutoScalingAutoScalingGroupDetails(TypedDict, closed=True):
    launch_configuration_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch configuration.</p>"""
    load_balancer_names: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The list of load balancers associated with the group.</p>"""
    health_check_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The service to use for the health checks. Valid values are <code>EC2</code> or <code>ELB</code>.</p>"""
    health_check_grace_period: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before it checks the health status of an EC2 instance that has come into service.</p>"""
    created_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the auto scaling group was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    mixed_instances_policy: NotRequired[
        "aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails"
    ]
    """<p>The mixed instances policy for the automatic scaling group.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.AwsAutoScalingAutoScalingGroupAvailabilityZonesList"
    ]
    """<p>The list of Availability Zones for the automatic scaling group.</p>"""
    launch_template: NotRequired[
        "aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification"
    ]
    """<p>The launch template to use.</p>"""
    capacity_rebalance: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether capacity rebalancing is enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAutoScalingAutoScalingGroupDetails) -> dict:
    out: dict = {}
    if "launch_configuration_name" in value:
        out["LaunchConfigurationName"] = value["launch_configuration_name"]
    if "load_balancer_names" in value:
        import aws_sdk_securityhub.types.string_list

        out["LoadBalancerNames"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["load_balancer_names"]
        )
    if "health_check_type" in value:
        out["HealthCheckType"] = value["health_check_type"]
    if "health_check_grace_period" in value:
        out["HealthCheckGracePeriod"] = value["health_check_grace_period"]
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "mixed_instances_policy" in value:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details

        out["MixedInstancesPolicy"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.serialize_json(
                value["mixed_instances_policy"]
            )
        )
    if "availability_zones" in value:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list

        out["AvailabilityZones"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.serialize_json(
                value["availability_zones"]
            )
        )
    if "launch_template" in value:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification

        out["LaunchTemplate"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "capacity_rebalance" in value:
        out["CapacityRebalance"] = value["capacity_rebalance"]
    return out


def deserialize_json(data: dict) -> AwsAutoScalingAutoScalingGroupDetails:
    out: AwsAutoScalingAutoScalingGroupDetails = {}  # type: ignore[typeddict-item]
    if "LaunchConfigurationName" in data:
        out["launch_configuration_name"] = data["LaunchConfigurationName"]
    if "LoadBalancerNames" in data:
        import aws_sdk_securityhub.types.string_list

        out["load_balancer_names"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["LoadBalancerNames"]
            )
        )
    if "HealthCheckType" in data:
        out["health_check_type"] = data["HealthCheckType"]
    if "HealthCheckGracePeriod" in data:
        out["health_check_grace_period"] = data["HealthCheckGracePeriod"]
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    if "MixedInstancesPolicy" in data:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details

        out["mixed_instances_policy"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_details.deserialize_json(
                data["MixedInstancesPolicy"]
            )
        )
    if "AvailabilityZones" in data:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list

        out["availability_zones"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "LaunchTemplate" in data:
        import aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification

        out["launch_template"] = (
            aws_sdk_securityhub.types.aws_auto_scaling_auto_scaling_group_launch_template_launch_template_specification.deserialize_json(
                data["LaunchTemplate"]
            )
        )
    if "CapacityRebalance" in data:
        out["capacity_rebalance"] = data["CapacityRebalance"]
    return out
