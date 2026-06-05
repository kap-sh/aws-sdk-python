"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceExportTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task


class CreateInstanceExportTaskResult(TypedDict):
    export_task: NotRequired["aws_sdk_ec2.types.export_task.ExportTask"]
    """<p>Information about the export instance task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceExportTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_task" in value:
        import aws_sdk_ec2.types.export_task

        aws_sdk_ec2.types.export_task.serialize_ec2_query(
            value["export_task"], pairs, f"{prefix}.ExportTask"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceExportTaskResult:
    out: CreateInstanceExportTaskResult = {}  # type: ignore[typeddict-item]
    child_export_task = el.find("ExportTask")
    if child_export_task is not None:
        import aws_sdk_ec2.types.export_task

        out["export_task"] = aws_sdk_ec2.types.export_task.deserialize_ec2_query(
            child_export_task
        )
    return out
