"""Generated from Smithy shape ``com.amazonaws.ec2#PriceSchedule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.long


class PriceSchedule(TypedDict):
    active: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The current price schedule, as determined by the term remaining for the Reserved Instance in the listing.</p> <p>A specific price schedule is always in effect, but only one price schedule can be active at any time. Take, for example, a Reserved Instance listing that has five months remaining in its term. When you specify price schedules for five months and two months, this means that schedule 1, covering the first three months of the remaining term, will be active during months 5, 4, and 3. Then schedule 2, covering the last two months of the term, will be active for months 2 and 1.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency for transacting the Reserved Instance resale. At this time, the only supported currency is <code>USD</code>.</p>"""
    price: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The fixed price for the term.</p>"""
    term: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.</p>"""
