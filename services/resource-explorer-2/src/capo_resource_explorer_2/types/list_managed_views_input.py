"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListManagedViewsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListManagedViewsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>"""
    service_principal: NotRequired["str"]
    """<p>Specifies a service principal name. If specified, then the operation only returns the managed views that are managed by the input service. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedViewsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_json(data: dict) -> ListManagedViewsInput:
    out: ListManagedViewsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    return out
