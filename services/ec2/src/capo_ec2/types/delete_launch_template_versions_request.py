"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.launch_template_id
    import capo_ec2.types.launch_template_name
    import capo_ec2.types.version_string_list


class DeleteLaunchTemplateVersionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_id: NotRequired[
        "capo_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired[
        "capo_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    versions: NotRequired["capo_ec2.types.version_string_list.VersionStringList"]
    """<p>The version numbers of one or more launch template versions to delete. You can specify up to 200 launch template version numbers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "launch_template_id" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateId", str(value["launch_template_id"]))
        )
    if "launch_template_name" in value:
        pairs.append(
            (f"{key_prefix}LaunchTemplateName", str(value["launch_template_name"]))
        )
    if "versions" in value:
        import capo_ec2.types.version_string_list

        capo_ec2.types.version_string_list.serialize_ec2_query(
            value["versions"], pairs, f"{key_prefix}Versions"
        )


def deserialize_ec2_query(el: Element) -> DeleteLaunchTemplateVersionsRequest:
    out: DeleteLaunchTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_launch_template_id = el.find("LaunchTemplateId")
    if child_launch_template_id is not None:
        out["launch_template_id"] = str(child_launch_template_id.text or "")
    child_launch_template_name = el.find("LaunchTemplateName")
    if child_launch_template_name is not None:
        out["launch_template_name"] = str(child_launch_template_name.text or "")
    if el.find("Versions") is not None:
        import capo_ec2.types.version_string_list

        out["versions"] = capo_ec2.types.version_string_list.deserialize_ec2_query(
            el, "Versions"
        )
    return out
