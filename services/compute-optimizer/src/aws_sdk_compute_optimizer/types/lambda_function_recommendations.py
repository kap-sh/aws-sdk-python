"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation

LambdaFunctionRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.lambda_function_recommendation.LambdaFunctionRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionRecommendations:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation

    out: LambdaFunctionRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
