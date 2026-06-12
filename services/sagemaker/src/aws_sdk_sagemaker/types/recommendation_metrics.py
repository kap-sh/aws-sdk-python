"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.float
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_setup_time
    import aws_sdk_sagemaker.types.utilization_metric


class RecommendationMetrics(TypedDict):
    cost_per_hour: NotRequired["aws_sdk_sagemaker.types.float.Float"]
    """<p>Defines the cost per hour for the instance. </p>"""
    cost_per_inference: NotRequired["aws_sdk_sagemaker.types.float.Float"]
    """<p>Defines the cost per inference for the instance .</p>"""
    max_invocations: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The expected maximum number of requests per minute for the instance.</p>"""
    model_latency: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The expected model latency at maximum invocation per minute for the instance.</p>"""
    cpu_utilization: NotRequired[
        "aws_sdk_sagemaker.types.utilization_metric.UtilizationMetric"
    ]
    """<p>The expected CPU utilization at maximum invocations per minute for the instance.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""
    memory_utilization: NotRequired[
        "aws_sdk_sagemaker.types.utilization_metric.UtilizationMetric"
    ]
    """<p>The expected memory utilization at maximum invocations per minute for the instance.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""
    model_setup_time: NotRequired[
        "aws_sdk_sagemaker.types.model_setup_time.ModelSetupTime"
    ]
    """<p>The time it takes to launch new compute resources for a serverless endpoint. The time can vary depending on the model size, how long it takes to download the model, and the start-up time of the container.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationMetrics) -> dict:
    out: dict = {}
    if "cost_per_hour" in value:
        out["CostPerHour"] = value["cost_per_hour"]
    if "cost_per_inference" in value:
        out["CostPerInference"] = value["cost_per_inference"]
    if "max_invocations" in value:
        out["MaxInvocations"] = value["max_invocations"]
    if "model_latency" in value:
        out["ModelLatency"] = value["model_latency"]
    if "cpu_utilization" in value:
        out["CpuUtilization"] = value["cpu_utilization"]
    if "memory_utilization" in value:
        out["MemoryUtilization"] = value["memory_utilization"]
    if "model_setup_time" in value:
        out["ModelSetupTime"] = value["model_setup_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationMetrics:
    out: RecommendationMetrics = {}  # type: ignore[typeddict-item]
    if "CostPerHour" in data:
        out["cost_per_hour"] = data["CostPerHour"]
    if "CostPerInference" in data:
        out["cost_per_inference"] = data["CostPerInference"]
    if "MaxInvocations" in data:
        out["max_invocations"] = data["MaxInvocations"]
    if "ModelLatency" in data:
        out["model_latency"] = data["ModelLatency"]
    if "CpuUtilization" in data:
        out["cpu_utilization"] = data["CpuUtilization"]
    if "MemoryUtilization" in data:
        out["memory_utilization"] = data["MemoryUtilization"]
    if "ModelSetupTime" in data:
        out["model_setup_time"] = data["ModelSetupTime"]
    return out
