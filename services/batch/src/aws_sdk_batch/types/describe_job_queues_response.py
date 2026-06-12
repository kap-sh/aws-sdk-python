"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobQueuesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_queue_detail_list
    import aws_sdk_batch.types.string


class DescribeJobQueuesResponse(TypedDict):
    job_queues: NotRequired[
        "aws_sdk_batch.types.job_queue_detail_list.JobQueueDetailList"
    ]
    """<p>The list of job queues.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeJobQueues</code> request. When the results of a <code>DescribeJobQueues</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobQueuesResponse) -> dict:
    out: dict = {}
    if "job_queues" in value:
        import aws_sdk_batch.types.job_queue_detail_list

        out["jobQueues"] = aws_sdk_batch.types.job_queue_detail_list.serialize_json(
            value["job_queues"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobQueuesResponse:
    out: DescribeJobQueuesResponse = {}  # type: ignore[typeddict-item]
    if "jobQueues" in data:
        import aws_sdk_batch.types.job_queue_detail_list

        out["job_queues"] = aws_sdk_batch.types.job_queue_detail_list.deserialize_json(
            data["jobQueues"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
