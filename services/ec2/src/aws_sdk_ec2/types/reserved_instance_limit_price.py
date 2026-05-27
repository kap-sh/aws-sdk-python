"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceLimitPrice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double


class ReservedInstanceLimitPrice(TypedDict):
    amount: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount * price).</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>limitPrice</code> amount is specified. At this time, the only supported currency is <code>USD</code>.</p>"""
