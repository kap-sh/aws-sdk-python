"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails(
    TypedDict, closed=True
):
    launch_template_specification: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification"
    ]
    """<p>The launch template to use for a mixed instances policy.</p>"""
    overrides: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList"
    ]
    """<p>Property values to use to override the values in the launch template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails,
) -> dict:
    out: dict = {}
    if "launch_template_specification" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification

        out["LaunchTemplateSpecification"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification.serialize_json(
                value["launch_template_specification"]
            )
        )
    if "overrides" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list

        out["Overrides"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails:
    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails = {}  # type: ignore[typeddict-item]
    if "LaunchTemplateSpecification" in data:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification

        out["launch_template_specification"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_launch_template_specification.deserialize_json(
                data["LaunchTemplateSpecification"]
            )
        )
    if "Overrides" in data:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list

        out["overrides"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list.deserialize_json(
                data["Overrides"]
            )
        )
    return out
