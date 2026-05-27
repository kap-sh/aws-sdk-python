"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_success_item

DisableFastSnapshotRestoreSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.disable_fast_snapshot_restore_success_item.DisableFastSnapshotRestoreSuccessItem"
]
