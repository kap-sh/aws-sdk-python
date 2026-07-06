"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetPortfolioSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.assessment_summary


class GetPortfolioSummaryResponse(TypedDict, closed=True):
    assessment_summary: NotRequired[
        "aws_sdk_migrationhubstrategy.types.assessment_summary.AssessmentSummary"
    ]
    """<p> An assessment summary for the portfolio including the number of servers to rehost and the overall number of anti-patterns. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortfolioSummaryResponse) -> dict:
    out: dict = {}
    if "assessment_summary" in value:
        import aws_sdk_migrationhubstrategy.types.assessment_summary

        out["assessmentSummary"] = (
            aws_sdk_migrationhubstrategy.types.assessment_summary.serialize_json(
                value["assessment_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPortfolioSummaryResponse:
    out: GetPortfolioSummaryResponse = {}  # type: ignore[typeddict-item]
    if "assessmentSummary" in data:
        import aws_sdk_migrationhubstrategy.types.assessment_summary

        out["assessment_summary"] = (
            aws_sdk_migrationhubstrategy.types.assessment_summary.deserialize_json(
                data["assessmentSummary"]
            )
        )
    return out
