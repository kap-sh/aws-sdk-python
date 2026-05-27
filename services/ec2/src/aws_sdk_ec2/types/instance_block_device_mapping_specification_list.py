"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMappingSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_block_device_mapping_specification

InstanceBlockDeviceMappingSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_block_device_mapping_specification.InstanceBlockDeviceMappingSpecification"
]
