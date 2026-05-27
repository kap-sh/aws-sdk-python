"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesNetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_config_set
    import aws_sdk_ec2.types.scheduled_instances_ipv6_address_list
    import aws_sdk_ec2.types.scheduled_instances_security_group_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class ScheduledInstancesNetworkInterface(TypedDict):
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to instances launched in a VPC. The public IPv4 address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is <code>true</code>.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to delete the interface when the instance is terminated.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the device for the network interface attachment.</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_security_group_id_set.ScheduledInstancesSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to the network interface. The IPv6 addresses are automatically selected from the subnet range.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_ipv6_address_list.ScheduledInstancesIpv6AddressList"
    ]
    """<p>The specific IPv6 addresses from the subnet range.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_address_configs: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_config_set.PrivateIpAddressConfigSet"
    ]
    """<p>The private IPv4 addresses.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
