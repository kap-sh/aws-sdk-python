"""Generated from Smithy shape ``com.amazonaws.ec2#PricingDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.integer


class PricingDetail(TypedDict):
    count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of reservations available for the price.</p>"""
    price: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The price per instance.</p>"""
