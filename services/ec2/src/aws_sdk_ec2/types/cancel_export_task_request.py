"""Generated from Smithy shape ``com.amazonaws.ec2#CancelExportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_vm_task_id


class CancelExportTaskRequest(TypedDict):
    export_task_id: NotRequired["aws_sdk_ec2.types.export_vm_task_id.ExportVmTaskId"]
    """<p>The ID of the export task. This is the ID returned by the <code>CreateInstanceExportTask</code> and <code>ExportImage</code> operations.</p>"""
