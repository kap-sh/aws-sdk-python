"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_secondary_interface_attachment
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list
    import aws_sdk_ec2.types.secondary_interface_id
    import aws_sdk_ec2.types.secondary_interface_status
    import aws_sdk_ec2.types.secondary_interface_type
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.string


class InstanceSecondaryInterface(TypedDict):
    attachment: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_attachment.InstanceSecondaryInterfaceAttachment"
    ]
    """<p>The attachment information for the secondary interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address of the secondary interface.</p>"""
    secondary_interface_id: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_id.SecondaryInterfaceId"
    ]
    """<p>The ID of the secondary interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the secondary interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list.InstanceSecondaryInterfacePrivateIpAddressList"
    ]
    """<p>The private IPv4 addresses associated with the secondary interface.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_status.SecondaryInterfaceStatus"
    ]
    """<p>The status of the secondary interface.</p>"""
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    interface_type: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""
