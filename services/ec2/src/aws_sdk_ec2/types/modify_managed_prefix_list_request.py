"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedPrefixListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_prefix_list_entries
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.remove_prefix_list_entries
    import aws_sdk_ec2.types.string


class ModifyManagedPrefixListRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    current_version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The current version of the prefix list.</p>"""
    prefix_list_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the prefix list.</p>"""
    add_entries: NotRequired[
        "aws_sdk_ec2.types.add_prefix_list_entries.AddPrefixListEntries"
    ]
    """<p>One or more entries to add to the prefix list.</p>"""
    remove_entries: NotRequired[
        "aws_sdk_ec2.types.remove_prefix_list_entries.RemovePrefixListEntries"
    ]
    """<p>One or more entries to remove from the prefix list.</p>"""
    max_entries: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list. You cannot modify the entries of a prefix list and modify the size of a prefix list at the same time.</p> <p>If any of the resources that reference the prefix list cannot support the new maximum size, the modify operation fails. Check the state message for the IDs of the first ten resources that do not support the new maximum size.</p>"""
    ipam_prefix_list_resolver_sync_enabled: NotRequired[
        "aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether synchronization with an IPAM prefix list resolver should be enabled for this managed prefix list. When enabled, the prefix list CIDRs are automatically updated based on the associated resolver's CIDR selection rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyManagedPrefixListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "current_version" in value:
        pairs.append((f"{prefix}.CurrentVersion", str(value["current_version"])))
    if "prefix_list_name" in value:
        pairs.append((f"{prefix}.PrefixListName", str(value["prefix_list_name"])))
    if "add_entries" in value:
        import aws_sdk_ec2.types.add_prefix_list_entries

        aws_sdk_ec2.types.add_prefix_list_entries.serialize_ec2_query(
            value["add_entries"], pairs, f"{prefix}.AddEntries"
        )
    if "remove_entries" in value:
        import aws_sdk_ec2.types.remove_prefix_list_entries

        aws_sdk_ec2.types.remove_prefix_list_entries.serialize_ec2_query(
            value["remove_entries"], pairs, f"{prefix}.RemoveEntries"
        )
    if "max_entries" in value:
        pairs.append((f"{prefix}.MaxEntries", str(value["max_entries"])))
    if "ipam_prefix_list_resolver_sync_enabled" in value:
        pairs.append(
            (
                f"{prefix}.IpamPrefixListResolverSyncEnabled",
                "true" if value["ipam_prefix_list_resolver_sync_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyManagedPrefixListRequest:
    out: ModifyManagedPrefixListRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_current_version = el.find("CurrentVersion")
    if child_current_version is not None:
        out["current_version"] = int(child_current_version.text or "")
    child_prefix_list_name = el.find("PrefixListName")
    if child_prefix_list_name is not None:
        out["prefix_list_name"] = str(child_prefix_list_name.text or "")
    if el.find("AddEntries") is not None:
        import aws_sdk_ec2.types.add_prefix_list_entries

        out["add_entries"] = (
            aws_sdk_ec2.types.add_prefix_list_entries.deserialize_ec2_query(
                el, "AddEntries"
            )
        )
    if el.find("RemoveEntries") is not None:
        import aws_sdk_ec2.types.remove_prefix_list_entries

        out["remove_entries"] = (
            aws_sdk_ec2.types.remove_prefix_list_entries.deserialize_ec2_query(
                el, "RemoveEntries"
            )
        )
    child_max_entries = el.find("MaxEntries")
    if child_max_entries is not None:
        out["max_entries"] = int(child_max_entries.text or "")
    child_ipam_prefix_list_resolver_sync_enabled = el.find(
        "IpamPrefixListResolverSyncEnabled"
    )
    if child_ipam_prefix_list_resolver_sync_enabled is not None:
        out["ipam_prefix_list_resolver_sync_enabled"] = (
            child_ipam_prefix_list_resolver_sync_enabled.text or ""
        ).lower() == "true"
    return out
