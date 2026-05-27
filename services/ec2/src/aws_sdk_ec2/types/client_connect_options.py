"""Generated from Smithy shape ``com.amazonaws.ec2#ClientConnectOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ClientConnectOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether client connect options are enabled. The default is <code>false</code> (not enabled).</p>"""
    lambda_function_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.</p>"""
