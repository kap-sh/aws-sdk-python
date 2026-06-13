"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetExportTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_task_id


class GetExportTaskInput(TypedDict):
    task_identifier: "aws_sdk_neptune_graph.types.export_task_id.ExportTaskId"
    """<p>The unique identifier of the export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportTaskInput:
    out: GetExportTaskInput = {}  # type: ignore[typeddict-item]
    return out
