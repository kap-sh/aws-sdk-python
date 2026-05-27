"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control_id

VpcEncryptionControlIdList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
]
