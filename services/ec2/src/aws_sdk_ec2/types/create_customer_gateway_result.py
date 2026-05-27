"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCustomerGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway


class CreateCustomerGatewayResult(TypedDict):
    customer_gateway: NotRequired["aws_sdk_ec2.types.customer_gateway.CustomerGateway"]
    """<p>Information about the customer gateway.</p>"""
