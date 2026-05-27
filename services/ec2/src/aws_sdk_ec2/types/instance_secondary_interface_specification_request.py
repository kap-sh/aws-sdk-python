"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list_request
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.secondary_interface_type
    import aws_sdk_ec2.types.secondary_subnet_id


class InstanceSecondaryInterfaceSpecificationRequest(TypedDict):
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the secondary interface is deleted when the instance is terminated.</p> <p>The only supported value for this field is <code>true</code>.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The device index for the secondary interface attachment.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_list_request.InstanceSecondaryInterfacePrivateIpAddressListRequest"
    ]
    """<p>The private IPv4 addresses to assign to the secondary interface.</p>"""
    private_ip_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of private IPv4 addresses to assign to the secondary interface.</p>"""
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    interface_type: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card. The network card must support secondary interfaces.</p>"""
