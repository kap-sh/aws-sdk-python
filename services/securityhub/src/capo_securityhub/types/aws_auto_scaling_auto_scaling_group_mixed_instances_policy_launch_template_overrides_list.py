"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details

AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList: TypeAlias = list[
    "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList,
) -> list:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details

    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_mixed_instances_policy_launch_template_overrides_list_details.deserialize_json(
                item
            )
        )
    return out
