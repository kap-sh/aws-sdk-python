"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListBatchLoadTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_status
    import capo_timestream_write.types.page_limit
    import capo_timestream_write.types.string


class ListBatchLoadTasksRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_timestream_write.types.string.String"]
    """<p>A token to specify where to start paginating. This is the NextToken from a previously truncated response.</p>"""
    max_results: NotRequired["capo_timestream_write.types.page_limit.PageLimit"]
    """<p>The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>"""
    task_status: NotRequired[
        "capo_timestream_write.types.batch_load_status.BatchLoadStatus"
    ]
    """<p>Status of the batch load task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBatchLoadTasksRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "task_status" in value:
        import capo_timestream_write.types.batch_load_status

        out["TaskStatus"] = (
            capo_timestream_write.types.batch_load_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBatchLoadTasksRequest:
    out: ListBatchLoadTasksRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "TaskStatus" in data:
        import capo_timestream_write.types.batch_load_status

        out["task_status"] = (
            capo_timestream_write.types.batch_load_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    return out
