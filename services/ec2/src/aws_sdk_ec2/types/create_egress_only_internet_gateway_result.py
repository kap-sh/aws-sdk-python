"""Generated from Smithy shape ``com.amazonaws.ec2#CreateEgressOnlyInternetGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway
    import aws_sdk_ec2.types.string


class CreateEgressOnlyInternetGatewayResult(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    egress_only_internet_gateway: NotRequired[
        "aws_sdk_ec2.types.egress_only_internet_gateway.EgressOnlyInternetGateway"
    ]
    """<p>Information about the egress-only internet gateway.</p>"""
