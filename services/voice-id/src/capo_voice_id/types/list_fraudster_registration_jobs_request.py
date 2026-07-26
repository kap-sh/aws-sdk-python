"""Generated from Smithy shape ``com.amazonaws.voiceid#ListFraudsterRegistrationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.fraudster_registration_job_status
    import capo_voice_id.types.max_results_for_list
    import capo_voice_id.types.next_token


class ListFraudsterRegistrationJobsRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster registration Jobs.</p>"""
    job_status: NotRequired[
        "capo_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
    ]
    """<p>Provides the status of your fraudster registration job.</p>"""
    max_results: NotRequired[
        "capo_voice_id.types.max_results_for_list.MaxResultsForList"
    ]
    """<p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>"""
    next_token: NotRequired["capo_voice_id.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFraudsterRegistrationJobsRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    if "job_status" in value:
        out["JobStatus"] = value["job_status"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFraudsterRegistrationJobsRequest:
    out: ListFraudsterRegistrationJobsRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError(
            "ListFraudsterRegistrationJobsRequest.domain_id required"
        )
    if "JobStatus" in data:
        out["job_status"] = data["JobStatus"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
