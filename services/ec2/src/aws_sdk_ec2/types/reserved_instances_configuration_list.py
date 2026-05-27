"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_configuration

ReservedInstancesConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_configuration.ReservedInstancesConfiguration"
]
