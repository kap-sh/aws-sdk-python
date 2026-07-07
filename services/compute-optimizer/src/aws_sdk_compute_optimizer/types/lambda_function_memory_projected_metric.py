"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name
    import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic
    import aws_sdk_compute_optimizer.types.metric_value


class LambdaFunctionMemoryProjectedMetric(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name.LambdaFunctionMemoryMetricName"
    ]
    """<p>The name of the projected utilization metric.</p>"""
    statistic: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic.LambdaFunctionMemoryMetricStatistic"
    ]
    """<p>The statistic of the projected utilization metric.</p>"""
    value: "aws_sdk_compute_optimizer.types.metric_value.MetricValue"
    """<p>The values of the projected utilization metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryProjectedMetric) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "statistic" in value:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic.serialize_aws_json_1_0(
                value["statistic"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionMemoryProjectedMetric:
    out: LambdaFunctionMemoryProjectedMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name

        out["name"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_metric_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if "statistic" in data:
        import aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic

        out["statistic"] = (
            aws_sdk_compute_optimizer.types.lambda_function_memory_metric_statistic.deserialize_aws_json_1_0(
                data["statistic"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
