"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_subnet_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_configuration
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.ipv4_prefixes_list
    import aws_sdk_ec2.types.ipv6_prefixes_list
    import aws_sdk_ec2.types.network_interface_association
    import aws_sdk_ec2.types.network_interface_attachment
    import aws_sdk_ec2.types.network_interface_ipv6_addresses_list
    import aws_sdk_ec2.types.network_interface_private_ip_address_list
    import aws_sdk_ec2.types.network_interface_status
    import aws_sdk_ec2.types.network_interface_type
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.public_ip_dns_name_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkInterface(TypedDict):
    association: NotRequired[
        "aws_sdk_ec2.types.network_interface_association.NetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IP address (IPv4) associated with the network interface.</p>"""
    attachment: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment.NetworkInterfaceAttachment"
    ]
    """<p>The network interface attachment.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    connection_tracking_configuration: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_configuration.ConnectionTrackingConfiguration"
    ]
    """<p>A security group connection tracking configuration that enables you to set the timeout for connection tracking on an Elastic network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts\">Connection tracking timeouts</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>Any security groups for the network interface.</p>"""
    interface_type: NotRequired[
        "aws_sdk_ec2.types.network_interface_type.NetworkInterfaceType"
    ]
    """<p>The type of network interface.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.network_interface_ipv6_addresses_list.NetworkInterfaceIpv6AddressesList"
    ]
    """<p>The IPv6 addresses associated with the network interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the network interface.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private hostname. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A public hostname. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    public_ip_dns_name_options: NotRequired[
        "aws_sdk_ec2.types.public_ip_dns_name_options.PublicIpDnsNameOptions"
    ]
    """<p>Public hostname type options. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.network_interface_private_ip_address_list.NetworkInterfacePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the network interface.</p>"""
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ipv4_prefixes_list.Ipv4PrefixesList"]
    """<p>The IPv4 prefixes that are assigned to the network interface.</p>"""
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ipv6_prefixes_list.Ipv6PrefixesList"]
    """<p>The IPv6 prefixes that are assigned to the network interface.</p>"""
    requester_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The alias or Amazon Web Services account ID of the principal or service that created the network interface.</p>"""
    requester_managed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is being managed by Amazon Web Services.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.network_interface_status.NetworkInterfaceStatus"
    ]
    """<p>The status of the network interface.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    tag_set: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the network interface.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    deny_all_igw_traffic: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is <code>true</code>, inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks.</p>"""
    ipv6_native: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is an IPv6 only network interface.</p>"""
    ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 globally unique address associated with the network interface.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the network interface.</p>"""
    associated_subnets: NotRequired[
        "aws_sdk_ec2.types.associated_subnet_list.AssociatedSubnetList"
    ]
    """<p>The subnets associated with this network interface.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
