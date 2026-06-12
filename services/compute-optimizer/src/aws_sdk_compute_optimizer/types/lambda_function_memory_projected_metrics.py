"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric

LambdaFunctionMemoryProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric.LambdaFunctionMemoryProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionMemoryProjectedMetrics:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric

    out: LambdaFunctionMemoryProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.lambda_function_memory_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
