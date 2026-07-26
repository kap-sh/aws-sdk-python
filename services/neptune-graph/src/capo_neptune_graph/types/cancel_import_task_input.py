"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CancelImportTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.task_id


class CancelImportTaskInput(TypedDict, closed=True):
    task_identifier: "capo_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelImportTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelImportTaskInput:
    out: CancelImportTaskInput = {}  # type: ignore[typeddict-item]
    return out
