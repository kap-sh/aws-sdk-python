"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_allocation_id
    import capo_ec2.types.ipam_pool_allocation_resource_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamPoolAllocation(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR for the allocation. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is <code>10.24.34.0/23</code>. An IPv6 CIDR example is <code>2001:DB8::/32</code>.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of an allocation.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the pool allocation.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_resource_type.IpamPoolAllocationResourceType"
    ]
    """<p>The type of the resource.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The owner of the resource.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the IPAM pool allocation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolAllocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "ipam_pool_allocation_id" in value:
        pairs.append(
            (f"{key_prefix}IpamPoolAllocationId", str(value["ipam_pool_allocation_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import capo_ec2.types.ipam_pool_allocation_resource_type

        capo_ec2.types.ipam_pool_allocation_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPoolAllocation:
    out: IpamPoolAllocation = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_ipam_pool_allocation_id = el.find("ipamPoolAllocationId")
    if child_ipam_pool_allocation_id is not None:
        out["ipam_pool_allocation_id"] = str(child_ipam_pool_allocation_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_pool_allocation_resource_type

        out["resource_type"] = (
            capo_ec2.types.ipam_pool_allocation_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_region = el.find("resourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_owner = el.find("resourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
