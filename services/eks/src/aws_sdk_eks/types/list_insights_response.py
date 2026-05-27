"""Generated from Smithy shape ``com.amazonaws.eks#ListInsightsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.insight_summaries
    import aws_sdk_eks.types.string


class ListInsightsResponse(TypedDict):
    insights: NotRequired["aws_sdk_eks.types.insight_summaries.InsightSummaries"]
    """<p>The returned list of insights.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListInsights</code> request. When the results of a <code>ListInsights</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsResponse) -> dict:
    out: dict = {}
    if "insights" in value:
        import aws_sdk_eks.types.insight_summaries

        out["insights"] = aws_sdk_eks.types.insight_summaries.serialize_json(
            value["insights"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsResponse:
    out: ListInsightsResponse = {}  # type: ignore[typeddict-item]
    if "insights" in data:
        import aws_sdk_eks.types.insight_summaries

        out["insights"] = aws_sdk_eks.types.insight_summaries.deserialize_json(
            data["insights"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
