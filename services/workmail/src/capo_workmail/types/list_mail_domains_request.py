"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.max_results
    import capo_workmail.types.next_token
    import capo_workmail.types.organization_id


class ListMailDomainsRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which to list domains.</p>"""
    max_results: NotRequired["capo_workmail.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not require a token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailDomainsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailDomainsRequest:
    out: ListMailDomainsRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("ListMailDomainsRequest.organization_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
