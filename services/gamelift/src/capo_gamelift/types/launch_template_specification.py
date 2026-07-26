"""Generated from Smithy shape ``com.amazonaws.gamelift#LaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.launch_template_id
    import capo_gamelift.types.launch_template_name
    import capo_gamelift.types.launch_template_version


class LaunchTemplateSpecification(TypedDict, closed=True):
    launch_template_id: NotRequired[
        "capo_gamelift.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>A unique identifier for an existing Amazon EC2 launch template.</p>"""
    launch_template_name: NotRequired[
        "capo_gamelift.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>A readable identifier for an existing Amazon EC2 launch template. </p>"""
    version: NotRequired[
        "capo_gamelift.types.launch_template_version.LaunchTemplateVersion"
    ]
    """<p>The version of the Amazon EC2 launch template to use. If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchTemplateSpecification) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["LaunchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["LaunchTemplateName"] = value["launch_template_name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LaunchTemplateSpecification:
    out: LaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if "LaunchTemplateId" in data:
        out["launch_template_id"] = data["LaunchTemplateId"]
    if "LaunchTemplateName" in data:
        out["launch_template_name"] = data["LaunchTemplateName"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
