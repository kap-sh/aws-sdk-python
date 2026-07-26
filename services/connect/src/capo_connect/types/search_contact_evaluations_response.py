"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.evaluation_search_summary_list
    import capo_connect.types.next_token


class SearchContactEvaluationsResponse(TypedDict, closed=True):
    evaluation_search_summary_list: NotRequired[
        "capo_connect.types.evaluation_search_summary_list.EvaluationSearchSummaryList"
    ]
    """<p>Contains information about contact evaluations.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of contact evaluations that matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactEvaluationsResponse) -> dict:
    out: dict = {}
    if "evaluation_search_summary_list" in value:
        import capo_connect.types.evaluation_search_summary_list

        out["EvaluationSearchSummaryList"] = (
            capo_connect.types.evaluation_search_summary_list.serialize_json(
                value["evaluation_search_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchContactEvaluationsResponse:
    out: SearchContactEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationSearchSummaryList" in data:
        import capo_connect.types.evaluation_search_summary_list

        out["evaluation_search_summary_list"] = (
            capo_connect.types.evaluation_search_summary_list.deserialize_json(
                data["EvaluationSearchSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
