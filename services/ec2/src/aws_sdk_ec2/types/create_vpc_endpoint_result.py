"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint


class CreateVpcEndpointResult(TypedDict):
    vpc_endpoint: NotRequired["aws_sdk_ec2.types.vpc_endpoint.VpcEndpoint"]
    """<p>Information about the endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
