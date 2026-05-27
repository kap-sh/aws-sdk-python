"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_list


class DescribeExportTasksResult(TypedDict):
    export_tasks: NotRequired["aws_sdk_ec2.types.export_task_list.ExportTaskList"]
    """<p>Information about the export tasks.</p>"""
