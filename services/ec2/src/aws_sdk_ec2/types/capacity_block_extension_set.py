"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtensionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension

CapacityBlockExtensionSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_extension.CapacityBlockExtension"
]
