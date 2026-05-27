"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accelerator_type

AcceleratorTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.accelerator_type.AcceleratorType"
]
