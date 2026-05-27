"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_task_detail
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportSnapshotTask(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the import snapshot task.</p>"""
    import_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the import snapshot task.</p>"""
    snapshot_task_detail: NotRequired[
        "aws_sdk_ec2.types.snapshot_task_detail.SnapshotTaskDetail"
    ]
    """<p>Describes an import snapshot task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the import snapshot task.</p>"""
