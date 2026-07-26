"""Generated from Smithy shape ``com.amazonaws.iot#ListJobExecutionsForJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_execution_status
    import capo_iot.types.job_id
    import capo_iot.types.laser_max_results
    import capo_iot.types.next_token


class ListJobExecutionsForJobRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    status: NotRequired["capo_iot.types.job_execution_status.JobExecutionStatus"]
    """<p>The status of the job.</p>"""
    max_results: NotRequired["capo_iot.types.laser_max_results.LaserMaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobExecutionsForJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobExecutionsForJobRequest:
    out: ListJobExecutionsForJobRequest = {}  # type: ignore[typeddict-item]
    return out
