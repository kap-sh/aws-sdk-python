"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolver``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_family
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_state
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPrefixListResolver(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IPAM prefix list resolver.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM associated with this resolver.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the associated IPAM is located.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the IPAM prefix list resolver.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.address_family.AddressFamily"]
    """<p>The address family (IPv4 or IPv6) for the IPAM prefix list resolver.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_state.IpamPrefixListResolverState"
    ]
    """<p>The current state of the IPAM prefix list resolver. Valid values include <code>create-in-progress</code>, <code>create-complete</code>, <code>create-failed</code>, <code>modify-in-progress</code>, <code>modify-complete</code>, <code>modify-failed</code>, <code>delete-in-progress</code>, <code>delete-complete</code>, and <code>delete-failed</code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM prefix list resolver.</p>"""
    last_version_creation_status: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status.IpamPrefixListResolverVersionCreationStatus"
    ]
    """<p>The status for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""
    last_version_creation_status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolver, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "ipam_prefix_list_resolver_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamPrefixListResolverId",
                str(value["ipam_prefix_list_resolver_id"]),
            )
        )
    if "ipam_prefix_list_resolver_arn" in value:
        pairs.append(
            (
                f"{prefix}.IpamPrefixListResolverArn",
                str(value["ipam_prefix_list_resolver_arn"]),
            )
        )
    if "ipam_arn" in value:
        pairs.append((f"{prefix}.IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{prefix}.IpamRegion", str(value["ipam_region"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "address_family" in value:
        import aws_sdk_ec2.types.address_family

        aws_sdk_ec2.types.address_family.serialize_ec2_query(
            value["address_family"], pairs, f"{prefix}.AddressFamily"
        )
    if "state" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_state

        aws_sdk_ec2.types.ipam_prefix_list_resolver_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "last_version_creation_status" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status

        aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status.serialize_ec2_query(
            value["last_version_creation_status"],
            pairs,
            f"{prefix}.LastVersionCreationStatus",
        )
    if "last_version_creation_status_message" in value:
        pairs.append(
            (
                f"{prefix}.LastVersionCreationStatusMessage",
                str(value["last_version_creation_status_message"]),
            )
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolver:
    out: IpamPrefixListResolver = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_prefix_list_resolver_id = el.find("IpamPrefixListResolverId")
    if child_ipam_prefix_list_resolver_id is not None:
        out["ipam_prefix_list_resolver_id"] = str(
            child_ipam_prefix_list_resolver_id.text or ""
        )
    child_ipam_prefix_list_resolver_arn = el.find("IpamPrefixListResolverArn")
    if child_ipam_prefix_list_resolver_arn is not None:
        out["ipam_prefix_list_resolver_arn"] = str(
            child_ipam_prefix_list_resolver_arn.text or ""
        )
    child_ipam_arn = el.find("IpamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("IpamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_address_family = el.find("AddressFamily")
    if child_address_family is not None:
        import aws_sdk_ec2.types.address_family

        out["address_family"] = aws_sdk_ec2.types.address_family.deserialize_ec2_query(
            child_address_family
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_state

        out["state"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_last_version_creation_status = el.find("LastVersionCreationStatus")
    if child_last_version_creation_status is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status

        out["last_version_creation_status"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status.deserialize_ec2_query(
                child_last_version_creation_status
            )
        )
    child_last_version_creation_status_message = el.find(
        "LastVersionCreationStatusMessage"
    )
    if child_last_version_creation_status_message is not None:
        out["last_version_creation_status_message"] = str(
            child_last_version_creation_status_message.text or ""
        )
    return out
