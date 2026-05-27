"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_task

ImportSnapshotTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.import_snapshot_task.ImportSnapshotTask"
]
