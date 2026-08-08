"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.address_family
    import capo_ec2.types.ipam_prefix_list_resolver_id
    import capo_ec2.types.ipam_prefix_list_resolver_state
    import capo_ec2.types.ipam_prefix_list_resolver_version_creation_status
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamPrefixListResolver(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IPAM prefix list resolver.</p>"""
    ipam_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM associated with this resolver.</p>"""
    ipam_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the associated IPAM is located.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the IPAM prefix list resolver.</p>"""
    address_family: NotRequired["capo_ec2.types.address_family.AddressFamily"]
    """<p>The address family (IPv4 or IPv6) for the IPAM prefix list resolver.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_state.IpamPrefixListResolverState"
    ]
    """<p>The current state of the IPAM prefix list resolver. Valid values include <code>create-in-progress</code>, <code>create-complete</code>, <code>create-failed</code>, <code>modify-in-progress</code>, <code>modify-complete</code>, <code>modify-failed</code>, <code>delete-in-progress</code>, <code>delete-complete</code>, and <code>delete-failed</code>.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM prefix list resolver.</p>"""
    last_version_creation_status: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_version_creation_status.IpamPrefixListResolverVersionCreationStatus"
    ]
    """<p>The status for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""
    last_version_creation_status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The status message for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolver, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_prefix_list_resolver_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverId",
                str(value["ipam_prefix_list_resolver_id"]),
            )
        )
    if "ipam_prefix_list_resolver_arn" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverArn",
                str(value["ipam_prefix_list_resolver_arn"]),
            )
        )
    if "ipam_arn" in value:
        pairs.append((f"{key_prefix}IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{key_prefix}IpamRegion", str(value["ipam_region"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "address_family" in value:
        import capo_ec2.types.address_family

        capo_ec2.types.address_family.serialize_ec2_query(
            value["address_family"], pairs, f"{key_prefix}AddressFamily"
        )
    if "state" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_state

        capo_ec2.types.ipam_prefix_list_resolver_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "last_version_creation_status" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_version_creation_status

        capo_ec2.types.ipam_prefix_list_resolver_version_creation_status.serialize_ec2_query(
            value["last_version_creation_status"],
            pairs,
            f"{key_prefix}LastVersionCreationStatus",
        )
    if "last_version_creation_status_message" in value:
        pairs.append(
            (
                f"{key_prefix}LastVersionCreationStatusMessage",
                str(value["last_version_creation_status_message"]),
            )
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolver:
    out: IpamPrefixListResolver = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_prefix_list_resolver_id = el.find("ipamPrefixListResolverId")
    if child_ipam_prefix_list_resolver_id is not None:
        out["ipam_prefix_list_resolver_id"] = str(
            child_ipam_prefix_list_resolver_id.text or ""
        )
    child_ipam_prefix_list_resolver_arn = el.find("ipamPrefixListResolverArn")
    if child_ipam_prefix_list_resolver_arn is not None:
        out["ipam_prefix_list_resolver_arn"] = str(
            child_ipam_prefix_list_resolver_arn.text or ""
        )
    child_ipam_arn = el.find("ipamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("ipamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_address_family = el.find("addressFamily")
    if child_address_family is not None:
        import capo_ec2.types.address_family

        out["address_family"] = capo_ec2.types.address_family.deserialize_ec2_query(
            child_address_family
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_state

        out["state"] = (
            capo_ec2.types.ipam_prefix_list_resolver_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_last_version_creation_status = el.find("lastVersionCreationStatus")
    if child_last_version_creation_status is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_version_creation_status

        out["last_version_creation_status"] = (
            capo_ec2.types.ipam_prefix_list_resolver_version_creation_status.deserialize_ec2_query(
                child_last_version_creation_status
            )
        )
    child_last_version_creation_status_message = el.find(
        "lastVersionCreationStatusMessage"
    )
    if child_last_version_creation_status_message is not None:
        out["last_version_creation_status_message"] = str(
            child_last_version_creation_status_message.text or ""
        )
    return out
