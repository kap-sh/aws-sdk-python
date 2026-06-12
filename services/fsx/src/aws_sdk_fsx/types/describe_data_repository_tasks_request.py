"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeDataRepositoryTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task_filters
    import aws_sdk_fsx.types.max_results
    import aws_sdk_fsx.types.next_token
    import aws_sdk_fsx.types.task_ids


class DescribeDataRepositoryTasksRequest(TypedDict):
    task_ids: NotRequired["aws_sdk_fsx.types.task_ids.TaskIds"]
    """<p>(Optional) IDs of the tasks whose descriptions you want to retrieve (String).</p>"""
    filters: NotRequired[
        "aws_sdk_fsx.types.data_repository_task_filters.DataRepositoryTaskFilters"
    ]
    """<p>(Optional) You can use filters to narrow the <code>DescribeDataRepositoryTasks</code> response to include just tasks for specific file systems, or tasks in a specific lifecycle state.</p>"""
    max_results: NotRequired["aws_sdk_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataRepositoryTasksRequest) -> dict:
    out: dict = {}
    if "task_ids" in value:
        import aws_sdk_fsx.types.task_ids

        out["TaskIds"] = aws_sdk_fsx.types.task_ids.serialize_aws_json_1_1(
            value["task_ids"]
        )
    if "filters" in value:
        import aws_sdk_fsx.types.data_repository_task_filters

        out["Filters"] = (
            aws_sdk_fsx.types.data_repository_task_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataRepositoryTasksRequest:
    out: DescribeDataRepositoryTasksRequest = {}  # type: ignore[typeddict-item]
    if "TaskIds" in data:
        import aws_sdk_fsx.types.task_ids

        out["task_ids"] = aws_sdk_fsx.types.task_ids.deserialize_aws_json_1_1(
            data["TaskIds"]
        )
    if "Filters" in data:
        import aws_sdk_fsx.types.data_repository_task_filters

        out["filters"] = (
            aws_sdk_fsx.types.data_repository_task_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
