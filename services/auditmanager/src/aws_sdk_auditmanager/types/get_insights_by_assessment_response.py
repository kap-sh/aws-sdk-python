"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetInsightsByAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.insights_by_assessment


class GetInsightsByAssessmentResponse(TypedDict, closed=True):
    insights: NotRequired[
        "aws_sdk_auditmanager.types.insights_by_assessment.InsightsByAssessment"
    ]
    """<p> The assessment analytics data that the <code>GetInsightsByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightsByAssessmentResponse) -> dict:
    out: dict = {}
    if "insights" in value:
        import aws_sdk_auditmanager.types.insights_by_assessment

        out["insights"] = (
            aws_sdk_auditmanager.types.insights_by_assessment.serialize_json(
                value["insights"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInsightsByAssessmentResponse:
    out: GetInsightsByAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "insights" in data:
        import aws_sdk_auditmanager.types.insights_by_assessment

        out["insights"] = (
            aws_sdk_auditmanager.types.insights_by_assessment.deserialize_json(
                data["insights"]
            )
        )
    return out
