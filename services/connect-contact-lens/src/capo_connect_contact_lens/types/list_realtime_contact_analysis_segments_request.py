"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ListRealtimeContactAnalysisSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.contact_id
    import capo_connect_contact_lens.types.instance_id
    import capo_connect_contact_lens.types.max_results
    import capo_connect_contact_lens.types.next_token


class ListRealtimeContactAnalysisSegmentsRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_connect_contact_lens.types.instance_id.InstanceId"]
    """<p>The identifier of the Amazon Connect instance.</p>"""
    contact_id: NotRequired["capo_connect_contact_lens.types.contact_id.ContactId"]
    """<p>The identifier of the contact.</p>"""
    max_results: NotRequired["capo_connect_contact_lens.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect_contact_lens.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsRequest) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsRequest:
    out: ListRealtimeContactAnalysisSegmentsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
