"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_request_options


class CreateTransitGatewayRequest(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the transit gateway.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_request_options.TransitGatewayRequestOptions"
    ]
    """<p>The transit gateway options.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the transit gateway.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
