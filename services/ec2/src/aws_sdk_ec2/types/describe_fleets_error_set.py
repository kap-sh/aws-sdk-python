"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleet_error

DescribeFleetsErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fleet_error.DescribeFleetError"
]
