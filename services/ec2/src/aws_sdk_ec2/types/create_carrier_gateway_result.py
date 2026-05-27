"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCarrierGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway


class CreateCarrierGatewayResult(TypedDict):
    carrier_gateway: NotRequired["aws_sdk_ec2.types.carrier_gateway.CarrierGateway"]
    """<p>Information about the carrier gateway.</p>"""
