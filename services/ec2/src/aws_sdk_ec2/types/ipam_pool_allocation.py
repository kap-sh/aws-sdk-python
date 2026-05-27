"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation_id
    import aws_sdk_ec2.types.ipam_pool_allocation_resource_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPoolAllocation(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR for the allocation. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is <code>10.24.34.0/23</code>. An IPv6 CIDR example is <code>2001:DB8::/32</code>.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of an allocation.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the pool allocation.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_resource_type.IpamPoolAllocationResourceType"
    ]
    """<p>The type of the resource.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner of the resource.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the IPAM pool allocation.</p>"""
