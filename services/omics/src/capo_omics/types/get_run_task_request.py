"""Generated from Smithy shape ``com.amazonaws.omics#GetRunTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_id
    import capo_omics.types.task_id


class GetRunTaskRequest(TypedDict, closed=True):
    id: "capo_omics.types.run_id.RunId"
    """<p>The workflow run ID.</p>"""
    task_id: "capo_omics.types.task_id.TaskId"
    """<p>The task's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRunTaskRequest:
    out: GetRunTaskRequest = {}  # type: ignore[typeddict-item]
    return out
