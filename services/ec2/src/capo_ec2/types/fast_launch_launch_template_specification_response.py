"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchLaunchTemplateSpecificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_id
    import capo_ec2.types.string


class FastLaunchLaunchTemplateSpecificationResponse(TypedDict, closed=True):
    launch_template_id: NotRequired[
        "capo_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template that the AMI uses for Windows fast launch.</p>"""
    launch_template_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the launch template that the AMI uses for Windows fast launch.</p>"""
    version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version of the launch template that the AMI uses for Windows fast launch.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FastLaunchLaunchTemplateSpecificationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))


def deserialize_ec2_query(el: Element) -> FastLaunchLaunchTemplateSpecificationResponse:
    out: FastLaunchLaunchTemplateSpecificationResponse = {}  # type: ignore[typeddict-item]
    child_launch_template_id = el.find("launchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("launchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_version = el.find("version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
