"""Generated from Smithy shape ``com.amazonaws.organizations#ListHandshakesForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake_filter
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token


class ListHandshakesForOrganizationRequest(TypedDict, closed=True):
    filter: NotRequired["capo_organizations.types.handshake_filter.HandshakeFilter"]
    """<p>A <code>HandshakeFilter</code> object. Contains the filer used to select the handshakes for an operation.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHandshakesForOrganizationRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_organizations.types.handshake_filter

        out["Filter"] = (
            capo_organizations.types.handshake_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHandshakesForOrganizationRequest:
    out: ListHandshakesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import capo_organizations.types.handshake_filter

        out["filter"] = (
            capo_organizations.types.handshake_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
