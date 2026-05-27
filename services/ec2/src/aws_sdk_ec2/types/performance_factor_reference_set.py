"""Generated from Smithy shape ``com.amazonaws.ec2#PerformanceFactorReferenceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.performance_factor_reference

PerformanceFactorReferenceSet: TypeAlias = list[
    "aws_sdk_ec2.types.performance_factor_reference.PerformanceFactorReference"
]
