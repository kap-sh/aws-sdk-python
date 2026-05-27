"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.long


class PriceScheduleSpecification(TypedDict):
    term: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.</p>"""
    price: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The fixed price for the term.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency for transacting the Reserved Instance resale. At this time, the only supported currency is <code>USD</code>.</p>"""
