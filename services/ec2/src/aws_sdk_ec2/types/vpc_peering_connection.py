"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnection``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_peering_connection_state_reason
    import aws_sdk_ec2.types.vpc_peering_connection_vpc_info


class VpcPeeringConnection(TypedDict):
    accepter_vpc_info: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    expiration_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that an unaccepted VPC peering connection will expire.</p>"""
    requester_vpc_info: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_state_reason.VpcPeeringConnectionStateReason"
    ]
    """<p>The status of the VPC peering connection.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection.</p>"""
