"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationPerformanceTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_constraint_list


class AIRecommendationPerformanceTarget(TypedDict, closed=True):
    constraints: NotRequired[
        "capo_sagemaker.types.ai_recommendation_constraint_list.AIRecommendationConstraintList"
    ]
    """<p>An array of performance constraints that define the optimization objectives.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationPerformanceTarget) -> dict:
    out: dict = {}
    if "constraints" in value:
        import capo_sagemaker.types.ai_recommendation_constraint_list

        out["Constraints"] = (
            capo_sagemaker.types.ai_recommendation_constraint_list.serialize_aws_json_1_1(
                value["constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationPerformanceTarget:
    out: AIRecommendationPerformanceTarget = {}  # type: ignore[typeddict-item]
    if "Constraints" in data:
        import capo_sagemaker.types.ai_recommendation_constraint_list

        out["constraints"] = (
            capo_sagemaker.types.ai_recommendation_constraint_list.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    return out
