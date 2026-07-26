"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetPortfolioSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.assessment_summary


class GetPortfolioSummaryResponse(TypedDict, closed=True):
    assessment_summary: NotRequired[
        "capo_migrationhubstrategy.types.assessment_summary.AssessmentSummary"
    ]
    """<p> An assessment summary for the portfolio including the number of servers to rehost and the overall number of anti-patterns. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortfolioSummaryResponse) -> dict:
    out: dict = {}
    if "assessment_summary" in value:
        import capo_migrationhubstrategy.types.assessment_summary

        out["assessmentSummary"] = (
            capo_migrationhubstrategy.types.assessment_summary.serialize_json(
                value["assessment_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPortfolioSummaryResponse:
    out: GetPortfolioSummaryResponse = {}  # type: ignore[typeddict-item]
    if "assessmentSummary" in data:
        import capo_migrationhubstrategy.types.assessment_summary

        out["assessment_summary"] = (
            capo_migrationhubstrategy.types.assessment_summary.deserialize_json(
                data["assessmentSummary"]
            )
        )
    return out
