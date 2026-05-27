"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type

ArchitectureTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.architecture_type.ArchitectureType"
]
