"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerConditionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_condition

CapacityManagerConditionSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_condition.CapacityManagerCondition"
]
