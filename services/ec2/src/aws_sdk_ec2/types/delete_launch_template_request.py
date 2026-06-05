"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.launch_template_name


class DeleteLaunchTemplateRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "launch_template_id" in value:
        pairs.append((f"{prefix}.LaunchTemplateId", str(value["launch_template_id"])))
    if "launch_template_name" in value:
        pairs.append(
            (f"{prefix}.LaunchTemplateName", str(value["launch_template_name"]))
        )


def deserialize_ec2_query(el: Element) -> DeleteLaunchTemplateRequest:
    out: DeleteLaunchTemplateRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    return out
