"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFiltersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.filter_action
    import capo_inspector2.types.filter_arn_list
    import capo_inspector2.types.list_filter_max_results
    import capo_inspector2.types.next_token


class ListFiltersRequest(TypedDict, closed=True):
    arns: NotRequired["capo_inspector2.types.filter_arn_list.FilterArnList"]
    """<p>The Amazon resource number (ARN) of the filter.</p>"""
    action: NotRequired["capo_inspector2.types.filter_action.FilterAction"]
    """<p>The action the filter applies to matched findings.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired[
        "capo_inspector2.types.list_filter_max_results.ListFilterMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFiltersRequest) -> dict:
    out: dict = {}
    if "arns" in value:
        import capo_inspector2.types.filter_arn_list

        out["arns"] = capo_inspector2.types.filter_arn_list.serialize_json(
            value["arns"]
        )
    if "action" in value:
        out["action"] = value["action"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListFiltersRequest:
    out: ListFiltersRequest = {}  # type: ignore[typeddict-item]
    if "arns" in data:
        import capo_inspector2.types.filter_arn_list

        out["arns"] = capo_inspector2.types.filter_arn_list.deserialize_json(
            data["arns"]
        )
    if "action" in data:
        out["action"] = data["action"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
