"""Generated from Smithy shape ``com.amazonaws.securityhub#GetInsightResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.insight_results


class GetInsightResultsResponse(TypedDict, closed=True):
    insight_results: NotRequired[
        "capo_securityhub.types.insight_results.InsightResults"
    ]
    """<p>The insight results returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightResultsResponse) -> dict:
    out: dict = {}
    if "insight_results" in value:
        import capo_securityhub.types.insight_results

        out["InsightResults"] = capo_securityhub.types.insight_results.serialize_json(
            value["insight_results"]
        )
    return out


def deserialize_json(data: dict) -> GetInsightResultsResponse:
    out: GetInsightResultsResponse = {}  # type: ignore[typeddict-item]
    if "InsightResults" in data:
        import capo_securityhub.types.insight_results

        out["insight_results"] = (
            capo_securityhub.types.insight_results.deserialize_json(
                data["InsightResults"]
            )
        )
    return out
