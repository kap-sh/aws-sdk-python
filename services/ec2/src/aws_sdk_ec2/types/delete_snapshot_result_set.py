"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSnapshotResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_snapshot_return_code

DeleteSnapshotResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_snapshot_return_code.DeleteSnapshotReturnCode"
]
