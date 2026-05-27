"""Generated from Smithy shape ``com.amazonaws.ec2#snapshotTierStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_tier_status

snapshotTierStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.snapshot_tier_status.SnapshotTierStatus"
]
