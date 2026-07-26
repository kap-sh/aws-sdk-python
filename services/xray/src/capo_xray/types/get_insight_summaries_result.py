"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightSummariesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.insight_summary_list
    import capo_xray.types.token


class GetInsightSummariesResult(TypedDict, closed=True):
    insight_summaries: NotRequired[
        "capo_xray.types.insight_summary_list.InsightSummaryList"
    ]
    """<p>The summary of each insight within the group matching the provided filters. The summary contains the InsightID, start and end time, the root cause service, the root cause and client impact statistics, the top anomalous services, and the status of the insight.</p>"""
    next_token: NotRequired["capo_xray.types.token.Token"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightSummariesResult) -> dict:
    out: dict = {}
    if "insight_summaries" in value:
        import capo_xray.types.insight_summary_list

        out["InsightSummaries"] = capo_xray.types.insight_summary_list.serialize_json(
            value["insight_summaries"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightSummariesResult:
    out: GetInsightSummariesResult = {}  # type: ignore[typeddict-item]
    if "InsightSummaries" in data:
        import capo_xray.types.insight_summary_list

        out["insight_summaries"] = (
            capo_xray.types.insight_summary_list.deserialize_json(
                data["InsightSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
