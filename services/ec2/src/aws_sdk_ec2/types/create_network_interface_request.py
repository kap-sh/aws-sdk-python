"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification_request
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipv4_prefix_list
    import aws_sdk_ec2.types.ipv6_prefix_list
    import aws_sdk_ec2.types.network_interface_creation_type
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.private_ip_address_specification_list
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class CreateNetworkInterfaceRequest(TypedDict):
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ipv4_prefix_list.Ipv4PrefixList"]
    """<p>The IPv4 prefixes assigned to the network interface.</p> <p>You can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</p>"""
    ipv4_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface.</p> <p>You can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</p>"""
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ipv6_prefix_list.Ipv6PrefixList"]
    """<p>The IPv6 prefixes assigned to the network interface.</p> <p>You can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</p>"""
    ipv6_prefix_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface.</p> <p>You can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</p>"""
    interface_type: NotRequired[
        "aws_sdk_ec2.types.network_interface_creation_type.NetworkInterfaceCreationType"
    ]
    """<p>The type of network interface. The default is <code>interface</code>.</p> <p>If you specify <code>efa-only</code>, do not assign any IP addresses to the network interface. EFA-only network interfaces do not support IP addresses.</p> <p>The only supported values are <code>interface</code>, <code>efa</code>, <code>efa-only</code>, and <code>trunk</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new network interface.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    enable_primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If you’re creating a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    connection_tracking_specification: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A connection tracking specification for the network interface.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to associate with the network interface.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the network interface.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one for you from the subnet's IPv4 CIDR range. If you specify an IP address, you cannot indicate any IP addresses specified in <code>privateIpAddresses</code> as primary (only one IP address can be designated as primary).</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_specification_list.PrivateIpAddressSpecificationList"
    ]
    """<p>The private IPv4 addresses.</p> <p>You can't specify private IPv4 addresses if you've specified one of the following: a count of private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.</p>"""
    secondary_private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using <code>privateIpAddresses</code>.</p> <p>You can't specify a count of private IPv4 addresses if you've specified one of the following: specific private IPv4 addresses, specific IPv4 prefixes, or a count of IPv4 prefixes.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses from the IPv6 CIDR block range of your subnet.</p> <p>You can't specify IPv6 addresses using this parameter if you've specified one of the following: a count of IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range.</p> <p>You can't specify a count of IPv6 addresses using this parameter if you've specified one of the following: specific IPv6 addresses, specific IPv6 prefixes, or a count of IPv6 prefixes.</p> <p>If your subnet has the <code>AssignIpv6AddressOnCreation</code> attribute set, you can override that setting by specifying 0 as the IPv6 address count.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
