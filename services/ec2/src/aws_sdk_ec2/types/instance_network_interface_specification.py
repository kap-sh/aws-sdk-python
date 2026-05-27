"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification_request
    import aws_sdk_ec2.types.ena_srd_specification_request
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipv4_prefix_list
    import aws_sdk_ec2.types.ipv6_prefix_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_specification_list
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.string


class InstanceNetworkInterfaceSpecification(TypedDict):
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is <code>true</code>.</p> <p>Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the <i>Public IPv4 Address</i> tab on the <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing page</a>.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, the interface is deleted when the instance is terminated. You can specify <code>true</code> only if creating a new network interface when launching an instance.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The position of the network interface in the attachment order. A primary network interface has a device index of 0.</p> <p>If you specify a network interface when launching an instance, you must specify the device index.</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p> <p>If you are creating a Spot Fleet, omit this parameter because you can’t specify a network interface ID in a launch specification.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a> request.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>The private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a> request.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses. You can’t specify this parameter and also specify a secondary private IP address using the <code>PrivateIpAddress</code> parameter.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet associated with the network interface. Applies only if creating a network interface when launching an instance.</p>"""
    associate_carrier_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a carrier IP address to the network interface.</p> <p>You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see <a href=\"https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#provider-owned-ip\">Carrier IP address</a> in the <i>Amazon Web Services Wavelength Developer Guide</i>.</p>"""
    interface_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of network interface.</p> <p>If you specify <code>efa-only</code>, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.</p> <p>Valid values: <code>interface</code> | <code>efa</code> | <code>efa-only</code> </p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.</p> <p>If you are using <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html\">RequestSpotInstances</a> to create Spot Instances, omit this parameter because you can’t specify the network card index when using this API. To specify the network card index, use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a>.</p>"""
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ipv4_prefix_list.Ipv4PrefixList"]
    """<p>The IPv4 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv4PrefixCount</code> option.</p>"""
    ipv4_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv4 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv4Prefix</code> option.</p>"""
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ipv6_prefix_list.Ipv6PrefixList"]
    """<p>The IPv6 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the <code>Ipv6PrefixCount</code> option.</p>"""
    ipv6_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the <code>Ipv6Prefix</code> option.</p>"""
    primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The primary IPv6 address of the network interface. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information about primary IPv6 addresses, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a>.</p>"""
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_specification_request.EnaSrdSpecificationRequest"
    ]
    """<p>Specifies the ENA Express settings for the network interface that's attached to the instance.</p>"""
    connection_tracking_specification: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A security group connection tracking specification that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""
