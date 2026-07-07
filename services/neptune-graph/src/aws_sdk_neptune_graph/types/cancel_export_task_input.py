"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CancelExportTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.export_task_id


class CancelExportTaskInput(TypedDict, closed=True):
    task_identifier: "aws_sdk_neptune_graph.types.export_task_id.ExportTaskId"
    """<p>The unique identifier of the export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelExportTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelExportTaskInput:
    out: CancelExportTaskInput = {}  # type: ignore[typeddict-item]
    return out
