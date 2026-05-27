"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification
    import aws_sdk_ec2.types.group_id_string_list
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipv4_prefix_list_response
    import aws_sdk_ec2.types.ipv6_prefix_list_response
    import aws_sdk_ec2.types.launch_template_ena_srd_specification
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_specification_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class LaunchTemplateInstanceNetworkInterfaceSpecification(TypedDict):
    associate_carrier_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to associate a Carrier IP address with eth0 for a new network interface.</p> <p>Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see <a href=\"https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip\">Carrier IP address</a> in the <i>Wavelength Developer Guide</i>.</p>"""
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to associate a public IPv4 address with eth0 for a new network interface.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the network interface.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The device index for the network interface attachment.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>The IDs of one or more security groups.</p>"""
    interface_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of network interface.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses for the network interface.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses for the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The primary private IPv4 address of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>One or more private IPv4 addresses.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses for the network interface.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet for the network interface.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    ipv4_prefixes: NotRequired[
        "aws_sdk_ec2.types.ipv4_prefix_list_response.Ipv4PrefixListResponse"
    ]
    """<p>One or more IPv4 prefixes assigned to the network interface.</p>"""
    ipv4_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.ipv6_prefix_list_response.Ipv6PrefixListResponse"
    ]
    """<p>One or more IPv6 prefixes assigned to the network interface.</p>"""
    ipv6_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigned to the network interface.</p>"""
    primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a>.</p>"""
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.launch_template_ena_srd_specification.LaunchTemplateEnaSrdSpecification"
    ]
    """<p>Contains the ENA Express settings for instances launched from your launch template.</p>"""
    connection_tracking_specification: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification.ConnectionTrackingSpecification"
    ]
    """<p>A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Idle connection tracking timeout</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues created with the instance.</p>"""
