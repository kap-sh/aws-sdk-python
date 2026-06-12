"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter

LambdaFunctionRecommendationFilters: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter.LambdaFunctionRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFilters) -> list:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionRecommendationFilters:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter

    out: LambdaFunctionRecommendationFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
