"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSEffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode
    import aws_sdk_compute_optimizer.types.look_back_period_preference


class ECSEffectiveRecommendationPreferences(TypedDict):
    savings_estimation_mode: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode.ECSSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon ECS services. </p>"""
    look_back_period: NotRequired[
        "aws_sdk_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The number of days the Amazon ECS service utilization metrics were analyzed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode

        out["savingsEstimationMode"] = (
            aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    if "look_back_period" in value:
        import aws_sdk_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            aws_sdk_compute_optimizer.types.look_back_period_preference.serialize_aws_json_1_0(
                value["look_back_period"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSEffectiveRecommendationPreferences:
    out: ECSEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if "savingsEstimationMode" in data:
        import aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode

        out["savings_estimation_mode"] = (
            aws_sdk_compute_optimizer.types.ecs_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    if "lookBackPeriod" in data:
        import aws_sdk_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            aws_sdk_compute_optimizer.types.look_back_period_preference.deserialize_aws_json_1_0(
                data["lookBackPeriod"]
            )
        )
    return out
