"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_info

SnapshotSet: TypeAlias = list["aws_sdk_ec2.types.snapshot_info.SnapshotInfo"]
