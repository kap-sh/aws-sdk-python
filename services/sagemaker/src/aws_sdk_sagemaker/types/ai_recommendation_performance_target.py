"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationPerformanceTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_constraint_list


class AIRecommendationPerformanceTarget(TypedDict):
    constraints: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_constraint_list.AIRecommendationConstraintList"
    ]
    """<p>An array of performance constraints that define the optimization objectives.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationPerformanceTarget) -> dict:
    out: dict = {}
    if "constraints" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_constraint_list

        out["Constraints"] = (
            aws_sdk_sagemaker.types.ai_recommendation_constraint_list.serialize_aws_json_1_1(
                value["constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationPerformanceTarget:
    out: AIRecommendationPerformanceTarget = {}  # type: ignore[typeddict-item]
    if "Constraints" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_constraint_list

        out["constraints"] = (
            aws_sdk_sagemaker.types.ai_recommendation_constraint_list.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    return out
