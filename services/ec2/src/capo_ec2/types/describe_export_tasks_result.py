"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_task_list


class DescribeExportTasksResult(TypedDict, closed=True):
    export_tasks: NotRequired["capo_ec2.types.export_task_list.ExportTaskList"]
    """<p>Information about the export tasks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeExportTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "export_tasks" in value:
        import capo_ec2.types.export_task_list

        capo_ec2.types.export_task_list.serialize_ec2_query(
            value["export_tasks"], pairs, f"{key_prefix}ExportTaskSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeExportTasksResult:
    out: DescribeExportTasksResult = {}  # type: ignore[typeddict-item]
    child_export_tasks = el.find("exportTaskSet")
    if child_export_tasks is not None:
        import capo_ec2.types.export_task_list

        out["export_tasks"] = capo_ec2.types.export_task_list.deserialize_ec2_query(
            child_export_tasks
        )
    return out
