"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.assessment_risk_recommendation_list
    import aws_sdk_resiliencehub.types.string500


class AssessmentSummary(TypedDict, closed=True):
    summary: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Indicates a concise summary that provides an overview of the Resilience Hub assessment.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""
    risk_recommendations: NotRequired[
        "aws_sdk_resiliencehub.types.assessment_risk_recommendation_list.AssessmentRiskRecommendationList"
    ]
    """<p>Indicates the top risks and recommendations identified by the Resilience Hub assessment, each representing a specific risk and the corresponding recommendation to address it.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentSummary) -> dict:
    out: dict = {}
    if "summary" in value:
        out["summary"] = value["summary"]
    if "risk_recommendations" in value:
        import aws_sdk_resiliencehub.types.assessment_risk_recommendation_list

        out["riskRecommendations"] = (
            aws_sdk_resiliencehub.types.assessment_risk_recommendation_list.serialize_json(
                value["risk_recommendations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssessmentSummary:
    out: AssessmentSummary = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        out["summary"] = data["summary"]
    if "riskRecommendations" in data:
        import aws_sdk_resiliencehub.types.assessment_risk_recommendation_list

        out["risk_recommendations"] = (
            aws_sdk_resiliencehub.types.assessment_risk_recommendation_list.deserialize_json(
                data["riskRecommendations"]
            )
        )
    return out
