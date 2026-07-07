"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchLaunchTemplateSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.string


class FastLaunchLaunchTemplateSpecificationRequest(TypedDict, closed=True):
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>Specify the ID of the launch template that the AMI should use for Windows fast launch.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the name of the launch template that the AMI should use for Windows fast launch.</p>"""
    version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the version of the launch template that the AMI should use for Windows fast launch.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FastLaunchLaunchTemplateSpecificationRequest,
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


def deserialize_ec2_query(el: Element) -> FastLaunchLaunchTemplateSpecificationRequest:
    out: FastLaunchLaunchTemplateSpecificationRequest = {}  # type: ignore[typeddict-item]
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
