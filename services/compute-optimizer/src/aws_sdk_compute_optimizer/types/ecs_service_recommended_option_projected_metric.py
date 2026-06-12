"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.cpu_size
    import aws_sdk_compute_optimizer.types.ecs_service_projected_metrics
    import aws_sdk_compute_optimizer.types.memory_size


class ECSServiceRecommendedOptionProjectedMetric(TypedDict):
    recommended_cpu_units: "aws_sdk_compute_optimizer.types.cpu_size.CpuSize"
    """<p> The recommended CPU size for the Amazon ECS service. </p>"""
    recommended_memory_size: "aws_sdk_compute_optimizer.types.memory_size.MemorySize"
    """<p> The recommended memory size for the Amazon ECS service. </p>"""
    projected_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_projected_metrics.ECSServiceProjectedMetrics"
    ]
    """<p> An array of objects that describe the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    out["recommendedCpuUnits"] = value.get("recommended_cpu_units", 0)
    out["recommendedMemorySize"] = value.get("recommended_memory_size", 0)
    if "projected_metrics" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_projected_metrics

        out["projectedMetrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendedOptionProjectedMetric:
    out: ECSServiceRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if "recommendedCpuUnits" in data:
        out["recommended_cpu_units"] = data["recommendedCpuUnits"]
    else:
        out["recommended_cpu_units"] = 0
    if "recommendedMemorySize" in data:
        out["recommended_memory_size"] = data["recommendedMemorySize"]
    else:
        out["recommended_memory_size"] = 0
    if "projectedMetrics" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_projected_metrics

        out["projected_metrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out
