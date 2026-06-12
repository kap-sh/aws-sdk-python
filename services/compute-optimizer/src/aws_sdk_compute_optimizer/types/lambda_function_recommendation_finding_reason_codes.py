"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code

LambdaFunctionRecommendationFindingReasonCodes: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code.LambdaFunctionRecommendationFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: LambdaFunctionRecommendationFindingReasonCodes,
) -> list:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> LambdaFunctionRecommendationFindingReasonCodes:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code

    out: LambdaFunctionRecommendationFindingReasonCodes = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out
