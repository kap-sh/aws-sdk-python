"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_transit_gateway_options
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_id


class ModifyTransitGatewayRequest(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the transit gateway.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.modify_transit_gateway_options.ModifyTransitGatewayOptions"
    ]
    """<p>The options to modify.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
