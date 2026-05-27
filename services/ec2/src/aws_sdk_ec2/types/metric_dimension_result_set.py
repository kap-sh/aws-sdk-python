"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDimensionResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_dimension

MetricDimensionResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_dimension.CapacityManagerDimension"
]
