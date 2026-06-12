"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTaskRunsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.task_run_filter_criteria
    import aws_sdk_glue.types.task_run_sort_criteria


class GetMLTaskRunsRequest(TypedDict):
    transform_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A token for pagination of the results. The default is empty.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return. </p>"""
    filter: NotRequired[
        "aws_sdk_glue.types.task_run_filter_criteria.TaskRunFilterCriteria"
    ]
    """<p>The filter criteria, in the <code>TaskRunFilterCriteria</code> structure, for the task run.</p>"""
    sort: NotRequired["aws_sdk_glue.types.task_run_sort_criteria.TaskRunSortCriteria"]
    """<p>The sorting criteria, in the <code>TaskRunSortCriteria</code> structure, for the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTaskRunsRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import aws_sdk_glue.types.task_run_filter_criteria

        out["Filter"] = (
            aws_sdk_glue.types.task_run_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "sort" in value:
        import aws_sdk_glue.types.task_run_sort_criteria

        out["Sort"] = aws_sdk_glue.types.task_run_sort_criteria.serialize_aws_json_1_1(
            value["sort"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTaskRunsRequest:
    out: GetMLTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("GetMLTaskRunsRequest.transform_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filter" in data:
        import aws_sdk_glue.types.task_run_filter_criteria

        out["filter"] = (
            aws_sdk_glue.types.task_run_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "Sort" in data:
        import aws_sdk_glue.types.task_run_sort_criteria

        out["sort"] = (
            aws_sdk_glue.types.task_run_sort_criteria.deserialize_aws_json_1_1(
                data["Sort"]
            )
        )
    return out
