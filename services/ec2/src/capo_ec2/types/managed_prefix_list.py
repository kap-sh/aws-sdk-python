"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedPrefixList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.prefix_list_state
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ManagedPrefixList(TypedDict, closed=True):
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    address_family: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address version.</p>"""
    state: NotRequired["capo_ec2.types.prefix_list_state.PrefixListState"]
    """<p>The current state of the prefix list.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The state message.</p>"""
    prefix_list_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the prefix list.</p>"""
    prefix_list_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the prefix list.</p>"""
    max_entries: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list.</p>"""
    version: NotRequired["capo_ec2.types.long.Long"]
    """<p>The version of the prefix list.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the prefix list.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the owner of the prefix list.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the IPAM prefix list resolver target associated with this managed prefix list. When set, this prefix list becomes an IPAM managed prefix list.</p> <p>An IPAM-managed prefix list is a customer-managed prefix list that has been associated with an IPAM prefix list resolver target. When a prefix list becomes IPAM managed, its CIDRs are automatically synchronized based on the IPAM prefix list resolver's CIDR selection rules, and direct CIDR modifications are restricted.</p>"""
    ipam_prefix_list_resolver_sync_enabled: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether synchronization with an IPAM prefix list resolver is enabled for this managed prefix list. When enabled, the prefix list CIDRs are automatically updated based on the resolver's CIDR selection rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ManagedPrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "address_family" in value:
        pairs.append((f"{key_prefix}AddressFamily", str(value["address_family"])))
    if "state" in value:
        import capo_ec2.types.prefix_list_state

        capo_ec2.types.prefix_list_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "prefix_list_arn" in value:
        pairs.append((f"{key_prefix}PrefixListArn", str(value["prefix_list_arn"])))
    if "prefix_list_name" in value:
        pairs.append((f"{key_prefix}PrefixListName", str(value["prefix_list_name"])))
    if "max_entries" in value:
        pairs.append((f"{key_prefix}MaxEntries", str(value["max_entries"])))
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_prefix_list_resolver_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverTargetId",
                str(value["ipam_prefix_list_resolver_target_id"]),
            )
        )
    if "ipam_prefix_list_resolver_sync_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverSyncEnabled",
                "true" if value["ipam_prefix_list_resolver_sync_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ManagedPrefixList:
    out: ManagedPrefixList = {}  # type: ignore[typeddict-item]
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_address_family = el.find("addressFamily")
    if child_address_family is not None:
        out["address_family"] = str(child_address_family.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.prefix_list_state

        out["state"] = capo_ec2.types.prefix_list_state.deserialize_ec2_query(
            child_state
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_prefix_list_arn = el.find("prefixListArn")
    if child_prefix_list_arn is not None:
        out["prefix_list_arn"] = str(child_prefix_list_arn.text or "")
    child_prefix_list_name = el.find("prefixListName")
    if child_prefix_list_name is not None:
        out["prefix_list_name"] = str(child_prefix_list_name.text or "")
    child_max_entries = el.find("maxEntries")
    if child_max_entries is not None:
        out["max_entries"] = int(child_max_entries.text or "")
    child_version = el.find("version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_prefix_list_resolver_target_id = el.find(
        "ipamPrefixListResolverTargetId"
    )
    if child_ipam_prefix_list_resolver_target_id is not None:
        out["ipam_prefix_list_resolver_target_id"] = str(
            child_ipam_prefix_list_resolver_target_id.text or ""
        )
    child_ipam_prefix_list_resolver_sync_enabled = el.find(
        "ipamPrefixListResolverSyncEnabled"
    )
    if child_ipam_prefix_list_resolver_sync_enabled is not None:
        out["ipam_prefix_list_resolver_sync_enabled"] = (
            child_ipam_prefix_list_resolver_sync_enabled.text or ""
        ).lower() == "true"
    return out
