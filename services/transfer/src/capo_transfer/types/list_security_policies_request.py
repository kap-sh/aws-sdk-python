"""Generated from Smithy shape ``com.amazonaws.transfer#ListSecurityPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token


class ListSecurityPoliciesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>Specifies the number of security policies to return as a response to the <code>ListSecurityPolicies</code> query.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When additional results are obtained from the <code>ListSecurityPolicies</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional security policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecurityPoliciesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecurityPoliciesRequest:
    out: ListSecurityPoliciesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
