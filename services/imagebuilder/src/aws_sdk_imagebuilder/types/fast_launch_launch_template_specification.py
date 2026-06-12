"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FastLaunchLaunchTemplateSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.launch_template_id
    import aws_sdk_imagebuilder.types.non_empty_string


class FastLaunchLaunchTemplateSpecification(TypedDict):
    launch_template_id: NotRequired[
        "aws_sdk_imagebuilder.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template to use for faster launching for a Windows AMI.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch template to use for faster launching for a Windows AMI.</p>"""
    launch_template_version: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the launch template to use for faster launching for a Windows AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FastLaunchLaunchTemplateSpecification) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["launchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["launchTemplateName"] = value["launch_template_name"]
    if "launch_template_version" in value:
        out["launchTemplateVersion"] = value["launch_template_version"]
    return out


def deserialize_json(data: dict) -> FastLaunchLaunchTemplateSpecification:
    out: FastLaunchLaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if "launchTemplateId" in data:
        out["launch_template_id"] = data["launchTemplateId"]
    if "launchTemplateName" in data:
        out["launch_template_name"] = data["launchTemplateName"]
    if "launchTemplateVersion" in data:
        out["launch_template_version"] = data["launchTemplateVersion"]
    return out
