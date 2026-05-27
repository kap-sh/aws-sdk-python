"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsInstancesSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleets_instances

DescribeFleetsInstancesSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fleets_instances.DescribeFleetsInstances"
]
