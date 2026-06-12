"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobRunsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.job_run_states
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string


class ListJobRunsRequest(TypedDict):
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the virtual cluster for which to list the job run. </p>"""
    created_before: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time before which the job runs were submitted.</p>"""
    created_after: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time after which the job runs were submitted.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the job run.</p>"""
    states: NotRequired["aws_sdk_emr_containers.types.job_run_states.JobRunStates"]
    """<p>The states of the job run.</p>"""
    max_results: NotRequired["aws_sdk_emr_containers.types.java_integer.JavaInteger"]
    """<p>The maximum number of job runs that can be listed.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p>The token for the next set of job runs to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobRunsRequest:
    out: ListJobRunsRequest = {}  # type: ignore[typeddict-item]
    return out
