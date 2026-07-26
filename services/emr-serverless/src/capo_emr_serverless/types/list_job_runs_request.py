"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.job_run_mode
    import capo_emr_serverless.types.job_run_state_set
    import capo_emr_serverless.types.next_token


class ListJobRunsRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application for which to list the job run.</p>"""
    next_token: NotRequired["capo_emr_serverless.types.next_token.NextToken"]
    """<p>The token for the next set of job run results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of job runs that can be listed.</p>"""
    created_at_after: NotRequired["capo_emr_serverless.types.date.Date"]
    """<p>The lower bound of the option to filter by creation date and time.</p>"""
    created_at_before: NotRequired["capo_emr_serverless.types.date.Date"]
    """<p>The upper bound of the option to filter by creation date and time.</p>"""
    states: NotRequired["capo_emr_serverless.types.job_run_state_set.JobRunStateSet"]
    """<p>An optional filter for job run states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.</p>"""
    mode: NotRequired["capo_emr_serverless.types.job_run_mode.JobRunMode"]
    """<p>The mode of the job runs to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobRunsRequest:
    out: ListJobRunsRequest = {}  # type: ignore[typeddict-item]
    return out
