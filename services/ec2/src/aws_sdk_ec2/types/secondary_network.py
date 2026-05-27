"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetwork``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_id
    import aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list
    import aws_sdk_ec2.types.secondary_network_state
    import aws_sdk_ec2.types.secondary_network_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecondaryNetwork(TypedDict):
    secondary_network_id: NotRequired[
        "aws_sdk_ec2.types.secondary_network_id.SecondaryNetworkId"
    ]
    """<p>The ID of the secondary network.</p>"""
    secondary_network_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary network.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the secondary network.</p>"""
    type: NotRequired["aws_sdk_ec2.types.secondary_network_type.SecondaryNetworkType"]
    """<p>The type of the secondary network.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.secondary_network_state.SecondaryNetworkState"
    ]
    """<p>The state of the secondary network.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state of the secondary network.</p>"""
    ipv4_cidr_block_associations: NotRequired[
        "aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association_list.SecondaryNetworkIpv4CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the secondary network.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the secondary network.</p>"""
