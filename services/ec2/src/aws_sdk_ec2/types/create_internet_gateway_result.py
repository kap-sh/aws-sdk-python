"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInternetGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway


class CreateInternetGatewayResult(TypedDict):
    internet_gateway: NotRequired["aws_sdk_ec2.types.internet_gateway.InternetGateway"]
    """<p>Information about the internet gateway.</p>"""
