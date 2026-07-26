"""Generated from Smithy shape ``com.amazonaws.organizations#ListDelegatedAdministratorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token
    import capo_organizations.types.service_principal


class ListDelegatedAdministratorsRequest(TypedDict, closed=True):
    service_principal: NotRequired[
        "capo_organizations.types.service_principal.ServicePrincipal"
    ]
    """<p>Specifies a service principal name. If specified, then the operation lists the delegated administrators only for the specified service.</p> <p>If you don't specify a service principal, the operation lists all delegated administrators for all services in your organization.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDelegatedAdministratorsRequest) -> dict:
    out: dict = {}
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDelegatedAdministratorsRequest:
    out: ListDelegatedAdministratorsRequest = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
