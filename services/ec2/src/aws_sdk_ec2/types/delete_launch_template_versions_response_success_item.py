"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseSuccessItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class DeleteLaunchTemplateVersionsResponseSuccessItem(TypedDict):
    launch_template_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the launch template.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the launch template.</p>"""
    version_number: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsResponseSuccessItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "launch_template_id" in value:
        pairs.append((f"{prefix}.LaunchTemplateId", str(value["launch_template_id"])))
    if "launch_template_name" in value:
        pairs.append(
            (f"{prefix}.LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "version_number" in value:
        pairs.append((f"{prefix}.VersionNumber", str(value["version_number"])))


def deserialize_ec2_query(
    el: Element,
) -> DeleteLaunchTemplateVersionsResponseSuccessItem:
    out: DeleteLaunchTemplateVersionsResponseSuccessItem = {}  # type: ignore[typeddict-item]
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    child_version_number = el.find("VersionNumber")
    if child_version_number is not None:
        out["version_number"] = int(child_version_number.text or "")
    return out
