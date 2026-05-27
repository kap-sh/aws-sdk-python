"""Generated from Smithy shape ``com.amazonaws.ec2#VirtualizationTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.virtualization_type

VirtualizationTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.virtualization_type.VirtualizationType"
]
