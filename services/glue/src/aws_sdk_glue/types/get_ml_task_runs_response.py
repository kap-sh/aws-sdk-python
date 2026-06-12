"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTaskRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.task_run_list


class GetMLTaskRunsResponse(TypedDict):
    task_runs: NotRequired["aws_sdk_glue.types.task_run_list.TaskRunList"]
    """<p>A list of task runs that are associated with the transform.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTaskRunsResponse) -> dict:
    out: dict = {}
    if "task_runs" in value:
        import aws_sdk_glue.types.task_run_list

        out["TaskRuns"] = aws_sdk_glue.types.task_run_list.serialize_aws_json_1_1(
            value["task_runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTaskRunsResponse:
    out: GetMLTaskRunsResponse = {}  # type: ignore[typeddict-item]
    if "TaskRuns" in data:
        import aws_sdk_glue.types.task_run_list

        out["task_runs"] = aws_sdk_glue.types.task_run_list.deserialize_aws_json_1_1(
            data["TaskRuns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
