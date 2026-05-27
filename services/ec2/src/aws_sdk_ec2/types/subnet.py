"""Generated from Smithy shape ``com.amazonaws.ec2#Subnet``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_public_access_states
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.coip_pool_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.private_dns_name_options_on_launch
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association_set
    import aws_sdk_ec2.types.subnet_state
    import aws_sdk_ec2.types.tag_list


class Subnet(TypedDict):
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The AZ ID of the subnet.</p>"""
    enable_lni_at_device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> Indicates the device position for local network interfaces in this subnet. For example, <code>1</code> indicates local network interfaces in this subnet are the secondary network interface (eth1). </p>"""
    map_customer_owned_ip_on_launch: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface created in this subnet (including a network interface created by <a>RunInstances</a>) receives a customer-owned IPv4 address.</p>"""
    customer_owned_ipv4_pool: NotRequired["aws_sdk_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The customer-owned IPv4 address pool associated with the subnet.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the subnet.</p>"""
    assign_ipv6_address_on_creation: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface created in this subnet (including a network interface created by <a>RunInstances</a>) receives an IPv6 address.</p>"""
    ipv6_cidr_block_association_set: NotRequired[
        "aws_sdk_ec2.types.subnet_ipv6_cidr_block_association_set.SubnetIpv6CidrBlockAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR blocks associated with the subnet.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the subnet.</p>"""
    subnet_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the subnet.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    enable_dns64: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.</p>"""
    ipv6_native: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is an IPv6 only subnet.</p>"""
    private_dns_name_options_on_launch: NotRequired[
        "aws_sdk_ec2.types.private_dns_name_options_on_launch.PrivateDnsNameOptionsOnLaunch"
    ]
    """<p>The type of hostnames to assign to instances in the subnet at launch. An instance hostname is based on the IPv4 address or ID of the instance.</p>"""
    block_public_access_states: NotRequired[
        "aws_sdk_ec2.types.block_public_access_states.BlockPublicAccessStates"
    ]
    """<p>The state of VPC Block Public Access (BPA).</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates if this is a subnet used with Amazon Elastic VMware Service (EVS). Possible values are <code>Elastic VMware Service</code> or no value. For more information about Amazon EVS, see <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html\"> <i>Amazon Elastic VMware Service API Reference</i> </a>.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    state: NotRequired["aws_sdk_ec2.types.subnet_state.SubnetState"]
    """<p>The current state of the subnet.</p> <ul> <li> <p> <code>failed</code>: The underlying infrastructure to support the subnet failed to provision as expected.</p> </li> <li> <p> <code>failed-insufficient-capacity</code>: The underlying infrastructure to support the subnet failed to provision due to a shortage of EC2 instance capacity.</p> </li> </ul>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC the subnet is in.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block assigned to the subnet.</p>"""
    available_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of unused private IPv4 addresses in the subnet. The IPv4 addresses for any stopped instances are considered unavailable.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the subnet.</p>"""
    default_for_az: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is the default subnet for the Availability Zone.</p>"""
    map_public_ip_on_launch: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether instances launched in this subnet receive a public IPv4 address.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
