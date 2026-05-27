"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_pool_allocation_allowed_cidrs
    import aws_sdk_ec2.types.ipam_pool_allocation_disallowed_cidrs
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class AllocateIpamPoolCidrRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool from which you would like to allocate a CIDR.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible values: Any available IPv4 or IPv6 CIDR.</p>"""
    netmask_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you would like to allocate from the IPAM pool. Note the following:</p> <ul> <li> <p>If there is no DefaultNetmaskLength allocation rule set on the pool, you must specify either the NetmaskLength or the CIDR.</p> </li> <li> <p>If the DefaultNetmaskLength allocation rule is set on the pool, you can specify either the NetmaskLength or the CIDR and the DefaultNetmaskLength allocation rule will be ignored.</p> </li> </ul> <p>Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the allocation.</p>"""
    preview_next_cidr: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A preview of the next available CIDR in a pool.</p>"""
    allowed_cidrs: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_allowed_cidrs.IpamPoolAllocationAllowedCidrs"
    ]
    """<p>Include a particular CIDR range that can be returned by the pool. Allowed CIDRs are only allowed if using netmask length for allocation.</p>"""
    disallowed_cidrs: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_disallowed_cidrs.IpamPoolAllocationDisallowedCidrs"
    ]
    """<p>Exclude a particular CIDR range from being returned by the pool. Disallowed CIDRs are only allowed if using netmask length for allocation.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> <p>If you specify tags, the request is authorized against the allocation resource in addition to the pool resource.</p>"""
