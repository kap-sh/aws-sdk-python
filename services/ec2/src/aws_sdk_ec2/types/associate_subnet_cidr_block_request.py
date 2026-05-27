"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSubnetCidrBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.netmask_length
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class AssociateSubnetCidrBlockRequest(TypedDict):
    ipv6_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv6 IPAM pool ID.</p>"""
    ipv6_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv6 netmask length.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of your subnet.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block for your subnet.</p>"""
