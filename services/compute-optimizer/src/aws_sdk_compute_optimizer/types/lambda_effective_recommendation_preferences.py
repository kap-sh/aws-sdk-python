"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaEffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode


class LambdaEffectiveRecommendationPreferences(TypedDict):
    savings_estimation_mode: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode.LambdaSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode applied for calculating savings opportunity for Lambda functions. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode

        out["savingsEstimationMode"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaEffectiveRecommendationPreferences:
    out: LambdaEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if "savingsEstimationMode" in data:
        import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode

        out["savings_estimation_mode"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out
