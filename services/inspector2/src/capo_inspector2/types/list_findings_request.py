"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.list_findings_max_results
    import capo_inspector2.types.next_token
    import capo_inspector2.types.sort_criteria


class ListFindingsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_inspector2.types.list_findings_max_results.ListFindingsMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    filter_criteria: NotRequired["capo_inspector2.types.filter_criteria.FilterCriteria"]
    """<p>Details on the filters to apply to your finding results.</p>"""
    sort_criteria: NotRequired["capo_inspector2.types.sort_criteria.SortCriteria"]
    """<p>Details on the sort criteria to apply to your finding results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filter_criteria" in value:
        import capo_inspector2.types.filter_criteria

        out["filterCriteria"] = capo_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "sort_criteria" in value:
        import capo_inspector2.types.sort_criteria

        out["sortCriteria"] = capo_inspector2.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> ListFindingsRequest:
    out: ListFindingsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filterCriteria" in data:
        import capo_inspector2.types.filter_criteria

        out["filter_criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["filterCriteria"]
        )
    if "sortCriteria" in data:
        import capo_inspector2.types.sort_criteria

        out["sort_criteria"] = capo_inspector2.types.sort_criteria.deserialize_json(
            data["sortCriteria"]
        )
    return out
