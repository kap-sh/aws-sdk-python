"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.domain_type
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipv4_pool_ec2_id
    import aws_sdk_ec2.types.public_ip_address
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class AllocateAddressRequest(TypedDict):
    domain: NotRequired["aws_sdk_ec2.types.domain_type.DomainType"]
    """<p>The network (<code>vpc</code>).</p>"""
    address: NotRequired["aws_sdk_ec2.types.public_ip_address.PublicIpAddress"]
    """<p>The Elastic IP address to recover or an IPv4 address from an address pool.</p>"""
    public_ipv4_pool: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To specify a specific address from the address pool, use the <code>Address</code> parameter instead.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.</p>"""
    customer_owned_ipv4_pool: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a customer-owned address pool. Use this parameter to let Amazon EC2 select an address from the address pool. Alternatively, specify a specific address from the address pool.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Elastic IP address.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPAM pool which has an Amazon-provided or BYOIP public IPv4 CIDR provisioned to it. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html\">Allocate sequential Elastic IP addresses from an IPAM pool</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
