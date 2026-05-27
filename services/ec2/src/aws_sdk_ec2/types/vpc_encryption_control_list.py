"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control

VpcEncryptionControlList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_encryption_control.VpcEncryptionControl"
]
