"""Generated from Smithy shape ``com.amazonaws.rds#ExportTasksMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.export_tasks_list
    import aws_sdk_rds.types.string


class ExportTasksMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeExportTasks</code> request. A marker is used for pagination to identify the location to begin output for the next response of <code>DescribeExportTasks</code>.</p>"""
    export_tasks: NotRequired["aws_sdk_rds.types.export_tasks_list.ExportTasksList"]
    """<p>Information about an export of a snapshot or cluster to Amazon S3.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExportTasksMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "export_tasks" in value:
        import aws_sdk_rds.types.export_tasks_list

        aws_sdk_rds.types.export_tasks_list.serialize_query(
            value["export_tasks"], pairs, f"{prefix}.ExportTasks"
        )


def deserialize_query(el: Element) -> ExportTasksMessage:
    out: ExportTasksMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_export_tasks = el.find("ExportTasks")
    if child_export_tasks is not None:
        import aws_sdk_rds.types.export_tasks_list

        out["export_tasks"] = aws_sdk_rds.types.export_tasks_list.deserialize_query(
            child_export_tasks
        )
    return out
