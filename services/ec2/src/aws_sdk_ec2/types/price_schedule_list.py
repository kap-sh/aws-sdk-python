"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.price_schedule

PriceScheduleList: TypeAlias = list["aws_sdk_ec2.types.price_schedule.PriceSchedule"]
