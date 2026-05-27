"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.secondary_interface_attachment
    import aws_sdk_ec2.types.secondary_interface_id
    import aws_sdk_ec2.types.secondary_interface_ipv4_address_list
    import aws_sdk_ec2.types.secondary_interface_status
    import aws_sdk_ec2.types.secondary_interface_type
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecondaryInterface(TypedDict):
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the secondary interface.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the secondary interface.</p>"""
    attachment: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_attachment.SecondaryInterfaceAttachment"
    ]
    """<p>The attachment information for the secondary interface.</p>"""
    mac_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The MAC address of the secondary interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary interface.</p>"""
    private_ipv4_addresses: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_ipv4_address_list.SecondaryInterfaceIpv4AddressList"
    ]
    """<p>The private IPv4 addresses associated with the secondary interface.</p>"""
    secondary_interface_id: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_id.SecondaryInterfaceId"
    ]
    """<p>The ID of the secondary interface.</p>"""
    secondary_interface_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary interface.</p>"""
    secondary_interface_type: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_type.SecondaryInterfaceType"
    ]
    """<p>The type of secondary interface.</p>"""
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_type: NotRequired[
        "aws_sdk_ec2.types.secondary_network_type.SecondaryNetworkType"
    ]
    """<p>The type of the secondary network.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_status.SecondaryInterfaceStatus"
    ]
    """<p>The status of the secondary interface.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary interface.</p>"""
