"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteTableAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_table_association_id
    import aws_sdk_ec2.types.route_table_id


class ReplaceRouteTableAssociationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    association_id: NotRequired[
        "aws_sdk_ec2.types.route_table_association_id.RouteTableAssociationId"
    ]
    """<p>The association ID.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the new route table to associate with the subnet.</p>"""
