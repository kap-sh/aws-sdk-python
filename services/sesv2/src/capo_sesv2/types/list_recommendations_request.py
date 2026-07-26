"""Generated from Smithy shape ``com.amazonaws.sesv2#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.list_recommendations_filter
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListRecommendationsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_sesv2.types.list_recommendations_filter.ListRecommendationsFilter"
    ]
    """<p>Filters applied when retrieving recommendations. Can eiter be an individual filter, or combinations of <code>STATUS</code> and <code>IMPACT</code> or <code>STATUS</code> and <code>TYPE</code> </p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListRecommendations</code> to indicate the position in the list of recommendations.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListRecommendations</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_sesv2.types.list_recommendations_filter

        out["Filter"] = capo_sesv2.types.list_recommendations_filter.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import capo_sesv2.types.list_recommendations_filter

        out["filter"] = capo_sesv2.types.list_recommendations_filter.deserialize_json(
            data["Filter"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    return out
