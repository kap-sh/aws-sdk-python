"""Generated from Smithy shape ``com.amazonaws.ec2#GetHostReservationPurchasePreviewResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.purchase_set
    import aws_sdk_ec2.types.string


class GetHostReservationPurchasePreviewResult(TypedDict):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>totalUpfrontPrice</code> and <code>totalHourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    purchase: NotRequired["aws_sdk_ec2.types.purchase_set.PurchaseSet"]
    """<p>The purchase information of the Dedicated Host reservation and the Dedicated Hosts associated with it.</p>"""
    total_hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The potential total hourly price of the reservation per hour.</p>"""
    total_upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The potential total upfront price. This is billed immediately.</p>"""
