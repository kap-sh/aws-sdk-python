"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcPeeringConnectionOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.peering_connection_options


class ModifyVpcPeeringConnectionOptionsResult(TypedDict):
    accepter_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options.PeeringConnectionOptions"
    ]
    """<p>Information about the VPC peering connection options for the accepter VPC.</p>"""
    requester_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options.PeeringConnectionOptions"
    ]
    """<p>Information about the VPC peering connection options for the requester VPC.</p>"""
