"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_memory_recommendation_option

LambdaFunctionMemoryRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.lambda_function_memory_recommendation_option.LambdaFunctionMemoryRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryRecommendationOptions) -> list:
    import capo_compute_optimizer.types.lambda_function_memory_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionMemoryRecommendationOptions:
    import capo_compute_optimizer.types.lambda_function_memory_recommendation_option

    out: LambdaFunctionMemoryRecommendationOptions = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.lambda_function_memory_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
