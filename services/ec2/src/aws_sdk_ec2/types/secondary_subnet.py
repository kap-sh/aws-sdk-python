"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnet``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.secondary_subnet_id
    import aws_sdk_ec2.types.secondary_subnet_ipv4_cidr_block_association_list
    import aws_sdk_ec2.types.secondary_subnet_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecondarySubnet(TypedDict):
    secondary_subnet_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_id.SecondarySubnetId"
    ]
    """<p>The ID of the secondary subnet.</p>"""
    secondary_subnet_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary subnet.</p>"""
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_type: NotRequired[
        "aws_sdk_ec2.types.secondary_network_type.SecondaryNetworkType"
    ]
    """<p>The type of the secondary network.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary subnet.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the secondary subnet.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone of the secondary subnet.</p>"""
    ipv4_cidr_block_associations: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_ipv4_cidr_block_association_list.SecondarySubnetIpv4CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the secondary subnet.</p>"""
    state: NotRequired["aws_sdk_ec2.types.secondary_subnet_state.SecondarySubnetState"]
    """<p>The state of the secondary subnet.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state of the secondary subnet.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary subnet.</p>"""
