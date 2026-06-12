"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option

LambdaFunctionMemoryRecommendationOptions: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option.LambdaFunctionMemoryRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryRecommendationOptions) -> list:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionMemoryRecommendationOptions:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option

    out: LambdaFunctionMemoryRecommendationOptions = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_memory_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
