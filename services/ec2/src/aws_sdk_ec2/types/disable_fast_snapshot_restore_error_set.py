"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_error_item

DisableFastSnapshotRestoreErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.disable_fast_snapshot_restore_error_item.DisableFastSnapshotRestoreErrorItem"
]
