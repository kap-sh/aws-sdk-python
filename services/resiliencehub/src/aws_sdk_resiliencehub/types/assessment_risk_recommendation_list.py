"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentRiskRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.assessment_risk_recommendation

AssessmentRiskRecommendationList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.assessment_risk_recommendation.AssessmentRiskRecommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentRiskRecommendationList) -> list:
    import aws_sdk_resiliencehub.types.assessment_risk_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.assessment_risk_recommendation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssessmentRiskRecommendationList:
    import aws_sdk_resiliencehub.types.assessment_risk_recommendation

    out: AssessmentRiskRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.assessment_risk_recommendation.deserialize_json(
                item
            )
        )
    return out
