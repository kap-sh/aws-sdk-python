"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringCharge``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.recurring_charge_frequency


class RecurringCharge(TypedDict):
    amount: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The amount of the recurring charge.</p>"""
    frequency: NotRequired[
        "aws_sdk_ec2.types.recurring_charge_frequency.RecurringChargeFrequency"
    ]
    """<p>The frequency of the recurring charge.</p>"""
