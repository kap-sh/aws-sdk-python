"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoreSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_snapshot_restore_success_item

DescribeFastSnapshotRestoreSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fast_snapshot_restore_success_item.DescribeFastSnapshotRestoreSuccessItem"
]
