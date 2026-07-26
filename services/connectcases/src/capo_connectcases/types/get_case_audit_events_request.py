"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseAuditEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.next_token


class GetCaseAuditEventsRequest(TypedDict, closed=True):
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseAuditEventsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCaseAuditEventsRequest:
    out: GetCaseAuditEventsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
