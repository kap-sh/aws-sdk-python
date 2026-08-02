"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_id
    import capo_ec2.types.string


class LaunchTemplateSpecification(TypedDict, closed=True):
    launch_template_id: NotRequired[
        "capo_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    version: NotRequired["capo_ec2.types.string.String"]
    """<p>The launch template version number, <code>$Latest</code>, or <code>$Default</code>.</p> <p>A value of <code>$Latest</code> uses the latest version of the launch template.</p> <p>A value of <code>$Default</code> uses the default version of the launch template.</p> <p>Default: The default version of the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateSpecification, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_ec2_query(el: Element) -> LaunchTemplateSpecification:
    out: LaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
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
