"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotRecycleBinInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_recycle_bin_info

SnapshotRecycleBinInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.snapshot_recycle_bin_info.SnapshotRecycleBinInfo"
]
