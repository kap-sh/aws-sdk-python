"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetECSServiceRecommendationProjectedMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics


class GetECSServiceRecommendationProjectedMetricsResponse(TypedDict):
    recommended_option_projected_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics.ECSServiceRecommendedOptionProjectedMetrics"
    ]
    """<p> An array of objects that describes the projected metrics. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetECSServiceRecommendationProjectedMetricsResponse,
) -> dict:
    out: dict = {}
    if "recommended_option_projected_metrics" in value:
        import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics

        out["recommendedOptionProjectedMetrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics.serialize_aws_json_1_0(
                value["recommended_option_projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetECSServiceRecommendationProjectedMetricsResponse:
    out: GetECSServiceRecommendationProjectedMetricsResponse = {}  # type: ignore[typeddict-item]
    if "recommendedOptionProjectedMetrics" in data:
        import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics

        out["recommended_option_projected_metrics"] = (
            aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metrics.deserialize_aws_json_1_0(
                data["recommendedOptionProjectedMetrics"]
            )
        )
    return out
