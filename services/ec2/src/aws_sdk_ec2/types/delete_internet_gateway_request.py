"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInternetGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.internet_gateway_id


class DeleteInternetGatewayRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    internet_gateway_id: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_id.InternetGatewayId"
    ]
    """<p>The ID of the internet gateway.</p>"""
