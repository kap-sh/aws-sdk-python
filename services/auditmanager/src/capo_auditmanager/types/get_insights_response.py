"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.insights


class GetInsightsResponse(TypedDict, closed=True):
    insights: NotRequired["capo_auditmanager.types.insights.Insights"]
    """<p>The analytics data that the <code>GetInsights</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightsResponse) -> dict:
    out: dict = {}
    if "insights" in value:
        import capo_auditmanager.types.insights

        out["insights"] = capo_auditmanager.types.insights.serialize_json(
            value["insights"]
        )
    return out


def deserialize_json(data: dict) -> GetInsightsResponse:
    out: GetInsightsResponse = {}  # type: ignore[typeddict-item]
    if "insights" in data:
        import capo_auditmanager.types.insights

        out["insights"] = capo_auditmanager.types.insights.deserialize_json(
            data["insights"]
        )
    return out
