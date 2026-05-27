"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyNetworkInterfaceAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_tracking_specification_request
    import aws_sdk_ec2.types.ena_srd_specification
    import aws_sdk_ec2.types.network_interface_attachment_changes
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.subnet_id_list


class ModifyNetworkInterfaceAttributeRequest(TypedDict):
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_specification.EnaSrdSpecification"
    ]
    """<p>Updates the ENA Express configuration for the network interface that’s attached to the instance.</p>"""
    enable_primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If you’re modifying a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    connection_tracking_specification: NotRequired[
        "aws_sdk_ec2.types.connection_tracking_specification_request.ConnectionTrackingSpecificationRequest"
    ]
    """<p>A connection tracking specification.</p>"""
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).</p>"""
    associated_subnet_ids: NotRequired["aws_sdk_ec2.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to associate with the network interface.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>A description for the network interface.</p>"""
    source_dest_check: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is <code>true</code>, source/destination checks are enabled; otherwise, they are disabled. The default value is <code>true</code>. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.</p>"""
    groups: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.</p>"""
    attachment: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment_changes.NetworkInterfaceAttachmentChanges"
    ]
    """<p>Information about the interface attachment. If modifying the <code>delete on termination</code> attribute, you must specify the ID of the interface attachment.</p>"""
