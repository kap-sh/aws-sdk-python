"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.price_schedule_specification

PriceScheduleSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.price_schedule_specification.PriceScheduleSpecification"
]
