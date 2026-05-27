"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceConnectEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint
    import aws_sdk_ec2.types.string


class CreateInstanceConnectEndpointResult(TypedDict):
    instance_connect_endpoint: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
    ]
    """<p>Information about the EC2 Instance Connect Endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive idempotency token provided by the client in the the request.</p>"""
