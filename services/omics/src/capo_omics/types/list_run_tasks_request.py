"""Generated from Smithy shape ``com.amazonaws.omics#ListRunTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_id
    import capo_omics.types.task_list_token
    import capo_omics.types.task_status


class ListRunTasksRequest(TypedDict, closed=True):
    id: "capo_omics.types.run_id.RunId"
    """<p>The run's ID.</p>"""
    status: NotRequired["capo_omics.types.task_status.TaskStatus"]
    """<p>Filter the list by status.</p>"""
    starting_token: NotRequired["capo_omics.types.task_list_token.TaskListToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of run tasks to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRunTasksRequest:
    out: ListRunTasksRequest = {}  # type: ignore[typeddict-item]
    return out
