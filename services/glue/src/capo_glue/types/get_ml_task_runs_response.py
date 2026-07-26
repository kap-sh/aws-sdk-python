"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTaskRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.pagination_token
    import capo_glue.types.task_run_list


class GetMLTaskRunsResponse(TypedDict, closed=True):
    task_runs: NotRequired["capo_glue.types.task_run_list.TaskRunList"]
    """<p>A list of task runs that are associated with the transform.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTaskRunsResponse) -> dict:
    out: dict = {}
    if "task_runs" in value:
        import capo_glue.types.task_run_list

        out["TaskRuns"] = capo_glue.types.task_run_list.serialize_aws_json_1_1(
            value["task_runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTaskRunsResponse:
    out: GetMLTaskRunsResponse = {}  # type: ignore[typeddict-item]
    if "TaskRuns" in data:
        import capo_glue.types.task_run_list

        out["task_runs"] = capo_glue.types.task_run_list.deserialize_aws_json_1_1(
            data["TaskRuns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
