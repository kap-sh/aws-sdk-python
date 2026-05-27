"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_error_item

EnableFastSnapshotRestoreErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.enable_fast_snapshot_restore_error_item.EnableFastSnapshotRestoreErrorItem"
]
