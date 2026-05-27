"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIpv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_source
    import aws_sdk_ec2.types.ipv6_address_attribute
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_cidr_block_state


class VpcIpv6CidrBlockAssociation(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association ID for the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    ipv6_cidr_block_state: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_state.VpcCidrBlockState"
    ]
    """<p>Information about the state of the CIDR block.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses, for example, <code>us-east-1-wl1-bos-wlz-1</code>.</p>"""
    ipv6_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.</p>"""
    ipv6_address_attribute: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_attribute.Ipv6AddressAttribute"
    ]
    """<p>Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.</p>"""
    ip_source: NotRequired["aws_sdk_ec2.types.ip_source.IpSource"]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""
