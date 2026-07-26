"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetImportTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.task_id


class GetImportTaskInput(TypedDict, closed=True):
    task_identifier: "capo_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportTaskInput:
    out: GetImportTaskInput = {}  # type: ignore[typeddict-item]
    return out
