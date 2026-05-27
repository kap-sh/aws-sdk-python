"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_association_state
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.vpc_id


class RouteServerAssociation(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the associated route server.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the associated VPC.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.route_server_association_state.RouteServerAssociationState"
    ]
    """<p>The current state of the association.</p>"""
