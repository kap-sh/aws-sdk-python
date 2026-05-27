"""Generated from Smithy shape ``com.amazonaws.ec2#HostOffering``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.payment_option
    import aws_sdk_ec2.types.string


class HostOffering(TypedDict):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency of the offering.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The duration of the offering (in seconds).</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price of the offering.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family of the offering.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the offering.</p>"""
    payment_option: NotRequired["aws_sdk_ec2.types.payment_option.PaymentOption"]
    """<p>The available payment option.</p>"""
    upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The upfront price of the offering. Does not apply to No Upfront offerings.</p>"""
