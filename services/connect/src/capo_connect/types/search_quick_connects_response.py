"""Generated from Smithy shape ``com.amazonaws.connect#SearchQuickConnectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.quick_connect_search_summary_list


class SearchQuickConnectsResponse(TypedDict, closed=True):
    quick_connects: NotRequired[
        "capo_connect.types.quick_connect_search_summary_list.QuickConnectSearchSummaryList"
    ]
    """<p>Information about the quick connects.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of quick connects which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickConnectsResponse) -> dict:
    out: dict = {}
    if "quick_connects" in value:
        import capo_connect.types.quick_connect_search_summary_list

        out["QuickConnects"] = (
            capo_connect.types.quick_connect_search_summary_list.serialize_json(
                value["quick_connects"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchQuickConnectsResponse:
    out: SearchQuickConnectsResponse = {}  # type: ignore[typeddict-item]
    if "QuickConnects" in data:
        import capo_connect.types.quick_connect_search_summary_list

        out["quick_connects"] = (
            capo_connect.types.quick_connect_search_summary_list.deserialize_json(
                data["QuickConnects"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
