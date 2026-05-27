"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_id_string_list
    import aws_sdk_ec2.types.filter_list


class DescribeExportTasksRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>the filters for the export tasks.</p>"""
    export_task_ids: NotRequired[
        "aws_sdk_ec2.types.export_task_id_string_list.ExportTaskIdStringList"
    ]
    """<p>The export task IDs.</p>"""
