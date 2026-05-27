"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_source
    import aws_sdk_ec2.types.ipv6_address_attribute
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_association_id
    import aws_sdk_ec2.types.subnet_cidr_block_state


class SubnetIpv6CidrBlockAssociation(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    ipv6_cidr_block_state: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_block_state.SubnetCidrBlockState"
    ]
    """<p>The state of the CIDR block.</p>"""
    ipv6_address_attribute: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_attribute.Ipv6AddressAttribute"
    ]
    """<p>Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.</p>"""
    ip_source: NotRequired["aws_sdk_ec2.types.ip_source.IpSource"]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""
