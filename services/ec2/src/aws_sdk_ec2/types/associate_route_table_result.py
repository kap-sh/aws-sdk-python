"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association_state
    import aws_sdk_ec2.types.string


class AssociateRouteTableResult(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The route table association ID. This ID is required for disassociating the route table.</p>"""
    association_state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""
