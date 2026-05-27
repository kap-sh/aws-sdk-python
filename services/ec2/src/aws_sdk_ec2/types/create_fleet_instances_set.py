"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetInstancesSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_fleet_instance

CreateFleetInstancesSet: TypeAlias = list[
    "aws_sdk_ec2.types.create_fleet_instance.CreateFleetInstance"
]
