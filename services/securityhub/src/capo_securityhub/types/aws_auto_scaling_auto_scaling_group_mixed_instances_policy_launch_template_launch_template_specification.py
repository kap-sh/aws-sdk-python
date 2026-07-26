"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(
    TypedDict, closed=True
):
    launch_template_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the launch template. You must specify either <code>LaunchTemplateId</code> or <code>LaunchTemplateName</code>.</p>"""
    launch_template_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch template. You must specify either <code>LaunchTemplateId</code> or <code>LaunchTemplateName</code>.</p>"""
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Identifies the version of the launch template. You can specify a version identifier, or use the values <code>$Latest</code> or <code>$Default</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification,
) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["LaunchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["LaunchTemplateName"] = value["launch_template_name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification:
    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if "LaunchTemplateId" in data:
        out["launch_template_id"] = data["LaunchTemplateId"]
    if "LaunchTemplateName" in data:
        out["launch_template_name"] = data["LaunchTemplateName"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
