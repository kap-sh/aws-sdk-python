"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_utilization_metric

LambdaFunctionUtilizationMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.lambda_function_utilization_metric.LambdaFunctionUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.lambda_function_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionUtilizationMetrics:
    import capo_compute_optimizer.types.lambda_function_utilization_metric

    out: LambdaFunctionUtilizationMetrics = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.lambda_function_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
