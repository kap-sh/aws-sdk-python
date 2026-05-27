"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification_response
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.instance_ipv4_prefix_list
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.instance_ipv6_prefix_list
    import aws_sdk_ec2.types.instance_network_interface_association
    import aws_sdk_ec2.types.instance_network_interface_attachment
    import aws_sdk_ec2.types.instance_private_ip_address_list
    import aws_sdk_ec2.types.network_interface_status
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string


class InstanceNetworkInterface(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_association.InstanceNetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IPv4 associated with the network interface.</p>"""
    attachment: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_attachment.InstanceNetworkInterfaceAttachment"
    ]
    """<p>The network interface attachment.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses associated with the network interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that created the network interface.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_private_ip_address_list.InstancePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the network interface.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.network_interface_status.NetworkInterfaceStatus"
    ]
    """<p>The status of the network interface.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    interface_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of network interface.</p> <p>Valid values: <code>interface</code> | <code>efa</code> | <code>efa-only</code> | <code>evs</code> | <code>trunk</code> </p>"""
    ipv4_prefixes: NotRequired[
        "aws_sdk_ec2.types.instance_ipv4_prefix_list.InstanceIpv4PrefixList"
    ]
    """<p>The IPv4 delegated prefixes that are assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_prefix_list.InstanceIpv6PrefixList"
    ]
    """<p>The IPv6 delegated prefixes that are assigned to the network interface.</p>"""
    connection_tracking_configuration: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification_response.ConnectionTrackingSpecificationResponse"
    ]
    """<p>A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the network interface.</p>"""
