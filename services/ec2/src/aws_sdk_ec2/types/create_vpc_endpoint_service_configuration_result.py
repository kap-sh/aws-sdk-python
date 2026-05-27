"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointServiceConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration
    import aws_sdk_ec2.types.string


class CreateVpcEndpointServiceConfigurationResult(TypedDict):
    service_configuration: NotRequired[
        "aws_sdk_ec2.types.service_configuration.ServiceConfiguration"
    ]
    """<p>Information about the service configuration.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
