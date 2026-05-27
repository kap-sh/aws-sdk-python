"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification_request
    import aws_sdk_ec2.types.ena_srd_specification_request
    import aws_sdk_ec2.types.instance_ipv6_address_list_request
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipv4_prefix_list
    import aws_sdk_ec2.types.ipv6_prefix_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_specification_list
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class LaunchTemplateInstanceNetworkInterfaceSpecificationRequest(TypedDict):
    associate_carrier_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Associates a Carrier IP address with eth0 for a new network interface.</p> <p>Use this option when you launch an instance in a Wavelength Zone and want to associate a Carrier IP address with the network interface. For more information about Carrier IP addresses, see <a href=\"https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip\">Carrier IP addresses</a> in the <i>Wavelength Developer Guide</i>.</p>"""
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Associates a public IPv4 address with eth0 for a new network interface.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the network interface.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The device index for the network interface attachment. The primary network interface has a device index of 0. Each network interface is of type <code>interface</code>, you must specify a device index. If you create a launch template that includes secondary network interfaces but not a primary network interface, then you must add a primary network interface as a launch parameter when you launch an instance from the template.</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of one or more security groups.</p>"""
    interface_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of network interface. To create an Elastic Fabric Adapter (EFA), specify <code>efa</code> or <code>efa</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html\">Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you are not creating an EFA, specify <code>interface</code> or omit this parameter.</p> <p>If you specify <code>efa-only</code>, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.</p> <p>Valid values: <code>interface</code> | <code>efa</code> | <code>efa-only</code> </p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list_request.InstanceIpv6AddressListRequest"
    ]
    """<p>One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't use this option if you're specifying a number of IPv6 addresses.</p>"""
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
    """<p>The number of secondary private IPv4 addresses to assign to a network interface.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet for the network interface.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.</p>"""
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ipv4_prefix_list.Ipv4PrefixList"]
    """<p>One or more IPv4 prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv4PrefixCount</code> option.</p>"""
    ipv4_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv4Prefix</code> option.</p>"""
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ipv6_prefix_list.Ipv6PrefixList"]
    """<p>One or more IPv6 prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv6PrefixCount</code> option.</p>"""
    ipv6_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv6Prefix</code> option.</p>"""
    primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a>.</p>"""
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_specification_request.EnaSrdSpecificationRequest"
    ]
    """<p>Configure ENA Express settings for your launch template.</p>"""
    connection_tracking_specification: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Idle connection tracking timeout</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""
