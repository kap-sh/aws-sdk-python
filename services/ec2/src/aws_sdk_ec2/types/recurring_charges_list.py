"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringChargesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.recurring_charge

RecurringChargesList: TypeAlias = list[
    "aws_sdk_ec2.types.recurring_charge.RecurringCharge"
]
