"""Generated from Smithy shape ``com.amazonaws.opensearch#ListInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.insight_list
    import capo_opensearch.types.next_token


class ListInsightsResponse(TypedDict, closed=True):
    insights: NotRequired["capo_opensearch.types.insight_list.InsightList"]
    """<p>The list of insights returned for the specified entity.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>When <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsResponse) -> dict:
    out: dict = {}
    if "insights" in value:
        import capo_opensearch.types.insight_list

        out["Insights"] = capo_opensearch.types.insight_list.serialize_json(
            value["insights"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsResponse:
    out: ListInsightsResponse = {}  # type: ignore[typeddict-item]
    if "Insights" in data:
        import capo_opensearch.types.insight_list

        out["insights"] = capo_opensearch.types.insight_list.deserialize_json(
            data["Insights"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
