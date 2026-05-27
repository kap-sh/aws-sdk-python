"""Generated from Smithy shape ``com.amazonaws.ec2#ClientConnectResponseOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_attribute_status
    import aws_sdk_ec2.types.string


class ClientConnectResponseOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether client connect options are enabled.</p>"""
    lambda_function_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_attribute_status.ClientVpnEndpointAttributeStatus"
    ]
    """<p>The status of any updates to the client connect options.</p>"""
