"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidr``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_pool_cidr_failure_reason
    import aws_sdk_ec2.types.ipam_pool_cidr_id
    import aws_sdk_ec2.types.ipam_pool_cidr_state
    import aws_sdk_ec2.types.string


class IpamPoolCidr(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR provisioned to the IPAM pool. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is <code>10.24.34.0/23</code>. An IPv6 CIDR example is <code>2001:DB8::/32</code>.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr_state.IpamPoolCidrState"]
    """<p>The state of the CIDR.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_cidr_failure_reason.IpamPoolCidrFailureReason"
    ]
    """<p>Details related to why an IPAM pool CIDR failed to be provisioned.</p>"""
    ipam_pool_cidr_id: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr_id.IpamPoolCidrId"]
    """<p>The IPAM pool CIDR ID.</p>"""
    netmask_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. \"NetmaskLength\" or \"Cidr\" is required.</p>"""
