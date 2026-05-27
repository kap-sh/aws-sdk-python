"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type

ArchitectureTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.architecture_type.ArchitectureType"
]
