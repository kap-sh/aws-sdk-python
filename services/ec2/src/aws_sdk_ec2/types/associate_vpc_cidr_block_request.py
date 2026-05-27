"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateVpcCidrBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipv6_pool_ec2_id
    import aws_sdk_ec2.types.netmask_length
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_id


class AssociateVpcCidrBlockRequest(TypedDict):
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An IPv4 CIDR block to associate with the VPC.</p>"""
    ipv6_cidr_block_network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the CIDR block to this location.</p> <p> You must set <code>AmazonProvidedIpv6CidrBlock</code> to <code>true</code> to use this parameter.</p> <p> You can have one IPv6 CIDR block association per network border group.</p>"""
    ipv6_pool: NotRequired["aws_sdk_ec2.types.ipv6_pool_ec2_id.Ipv6PoolEc2Id"]
    """<p>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An IPv6 CIDR block from the IPv6 address pool. You must also specify <code>Ipv6Pool</code> in the request.</p> <p>To let Amazon choose the IPv6 CIDR block for you, omit this parameter.</p>"""
    ipv4_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>Associate a CIDR allocated from an IPv4 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv4_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    ipv6_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>Associates a CIDR allocated from an IPv6 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IPAM), see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    amazon_provided_ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses or the size of the CIDR block.</p>"""
