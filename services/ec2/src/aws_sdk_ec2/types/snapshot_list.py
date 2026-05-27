"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot

SnapshotList: TypeAlias = list["aws_sdk_ec2.types.snapshot.Snapshot"]
