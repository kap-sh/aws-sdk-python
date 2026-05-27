"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcPeeringConnectionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_peering_connection


class AcceptVpcPeeringConnectionResult(TypedDict):
    vpc_peering_connection: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection.VpcPeeringConnection"
    ]
    """<p>Information about the VPC peering connection.</p>"""
