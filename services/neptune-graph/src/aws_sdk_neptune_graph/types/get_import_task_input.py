"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetImportTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.task_id


class GetImportTaskInput(TypedDict):
    task_identifier: "aws_sdk_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportTaskInput:
    out: GetImportTaskInput = {}  # type: ignore[typeddict-item]
    return out
