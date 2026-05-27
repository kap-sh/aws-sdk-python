"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_state
    import aws_sdk_ec2.types.export_to_s3_task
    import aws_sdk_ec2.types.instance_export_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ExportTask(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the resource being exported.</p>"""
    export_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the export task.</p>"""
    export_to_s3_task: NotRequired["aws_sdk_ec2.types.export_to_s3_task.ExportToS3Task"]
    """<p>Information about the export task.</p>"""
    instance_export_details: NotRequired[
        "aws_sdk_ec2.types.instance_export_details.InstanceExportDetails"
    ]
    """<p>Information about the instance to export.</p>"""
    state: NotRequired["aws_sdk_ec2.types.export_task_state.ExportTaskState"]
    """<p>The state of the export task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message related to the export task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the export task.</p>"""
