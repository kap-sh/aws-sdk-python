"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_task_id

ImportSnapshotTaskIdList: TypeAlias = list[
    "aws_sdk_ec2.types.import_snapshot_task_id.ImportSnapshotTaskId"
]
