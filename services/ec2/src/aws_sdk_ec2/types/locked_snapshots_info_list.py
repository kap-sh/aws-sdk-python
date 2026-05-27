"""Generated from Smithy shape ``com.amazonaws.ec2#LockedSnapshotsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.locked_snapshots_info

LockedSnapshotsInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.locked_snapshots_info.LockedSnapshotsInfo"
]
