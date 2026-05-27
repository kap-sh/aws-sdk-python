"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_detail

SnapshotDetailList: TypeAlias = list["aws_sdk_ec2.types.snapshot_detail.SnapshotDetail"]
