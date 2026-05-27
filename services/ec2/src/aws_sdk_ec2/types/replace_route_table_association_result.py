"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteTableAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association_state
    import aws_sdk_ec2.types.string


class ReplaceRouteTableAssociationResult(TypedDict):
    new_association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the new association.</p>"""
    association_state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state.RouteTableAssociationState"
    ]
    """<p>The state of the association.</p>"""
