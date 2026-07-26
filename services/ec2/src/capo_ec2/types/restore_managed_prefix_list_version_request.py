"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreManagedPrefixListVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.long
    import capo_ec2.types.prefix_list_resource_id


class RestoreManagedPrefixListVersionRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    previous_version: NotRequired["capo_ec2.types.long.Long"]
    """<p>The version to restore.</p>"""
    current_version: NotRequired["capo_ec2.types.long.Long"]
    """<p>The current version number for the prefix list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreManagedPrefixListVersionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "previous_version" in value:
        pairs.append((f"{prefix}.PreviousVersion", str(value["previous_version"])))
    if "current_version" in value:
        pairs.append((f"{prefix}.CurrentVersion", str(value["current_version"])))


def deserialize_ec2_query(el: Element) -> RestoreManagedPrefixListVersionRequest:
    out: RestoreManagedPrefixListVersionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_previous_version = el.find("PreviousVersion")
    if child_previous_version is not None:
        out["previous_version"] = int(child_previous_version.text or "")
    child_current_version = el.find("CurrentVersion")
    if child_current_version is not None:
        out["current_version"] = int(child_current_version.text or "")
    return out
