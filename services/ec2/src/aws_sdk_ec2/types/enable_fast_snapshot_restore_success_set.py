"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_success_item

EnableFastSnapshotRestoreSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.enable_fast_snapshot_restore_success_item.EnableFastSnapshotRestoreSuccessItem"
]
