"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceExportTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task


class CreateInstanceExportTaskResult(TypedDict):
    export_task: NotRequired["aws_sdk_ec2.types.export_task.ExportTask"]
    """<p>Information about the export instance task.</p>"""
