"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceExportTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_task


class CreateInstanceExportTaskResult(TypedDict, closed=True):
    export_task: NotRequired["capo_ec2.types.export_task.ExportTask"]
    """<p>Information about the export instance task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceExportTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "export_task" in value:
        import capo_ec2.types.export_task

        capo_ec2.types.export_task.serialize_ec2_query(
            value["export_task"], pairs, f"{key_prefix}ExportTask"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceExportTaskResult:
    out: CreateInstanceExportTaskResult = {}  # type: ignore[typeddict-item]
    child_export_task = el.find("ExportTask")
    if child_export_task is not None:
        import capo_ec2.types.export_task

        out["export_task"] = capo_ec2.types.export_task.deserialize_ec2_query(
            child_export_task
        )
    return out
