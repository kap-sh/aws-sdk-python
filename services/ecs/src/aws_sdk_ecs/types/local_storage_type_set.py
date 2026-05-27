"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorageTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.local_storage_type

LocalStorageTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.local_storage_type.LocalStorageType"
]
