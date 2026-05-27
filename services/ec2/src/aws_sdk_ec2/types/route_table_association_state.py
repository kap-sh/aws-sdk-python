"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociationState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association_state_code
    import aws_sdk_ec2.types.string


class RouteTableAssociationState(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state_code.RouteTableAssociationStateCode"
    ]
    """<p>The state of the association.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message, if applicable.</p>"""
