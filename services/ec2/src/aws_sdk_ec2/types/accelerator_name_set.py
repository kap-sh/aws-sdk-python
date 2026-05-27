"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorNameSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accelerator_name

AcceleratorNameSet: TypeAlias = list[
    "aws_sdk_ec2.types.accelerator_name.AcceleratorName"
]
