"""Generated from Smithy shape ``com.amazonaws.ec2#LocalStorageTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_storage_type

LocalStorageTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_storage_type.LocalStorageType"
]
