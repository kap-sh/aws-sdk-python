"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.string


class FleetLaunchTemplateSpecificationRequest(TypedDict):
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify the <code>LaunchTemplateId</code> or the <code>LaunchTemplateName</code>, but not both.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify the <code>LaunchTemplateName</code> or the <code>LaunchTemplateId</code>, but not both.</p>"""
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The launch template version number, <code>$Latest</code>, or <code>$Default</code>. You must specify a value, otherwise the request fails.</p> <p>If the value is <code>$Latest</code>, Amazon EC2 uses the latest version of the launch template.</p> <p>If the value is <code>$Default</code>, Amazon EC2 uses the default version of the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateSpecificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "launch_template_id" in value:
        pairs.append((f"{prefix}.LaunchTemplateId", str(value["launch_template_id"])))
    if "launch_template_name" in value:
        pairs.append(
            (f"{prefix}.LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateSpecificationRequest:
    out: FleetLaunchTemplateSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
