"""Generated from Smithy shape ``com.amazonaws.deadline#ListTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id


class ListTasksRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID connected to the tasks.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID connected to the tasks.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID for the tasks.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID for the tasks.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTasksRequest:
    out: ListTasksRequest = {}  # type: ignore[typeddict-item]
    return out
