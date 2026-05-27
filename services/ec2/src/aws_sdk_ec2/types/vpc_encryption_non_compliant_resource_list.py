"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionNonCompliantResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource

VpcEncryptionNonCompliantResourceList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_encryption_non_compliant_resource.VpcEncryptionNonCompliantResource"
]
