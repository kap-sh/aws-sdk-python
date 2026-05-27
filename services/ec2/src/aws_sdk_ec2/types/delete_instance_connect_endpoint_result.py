"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceConnectEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint


class DeleteInstanceConnectEndpointResult(TypedDict):
    instance_connect_endpoint: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
    ]
    """<p>Information about the EC2 Instance Connect Endpoint.</p>"""
