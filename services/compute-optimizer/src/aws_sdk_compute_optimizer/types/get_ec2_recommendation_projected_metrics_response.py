"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEC2RecommendationProjectedMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommended_option_projected_metrics


class GetEC2RecommendationProjectedMetricsResponse(TypedDict, closed=True):
    recommended_option_projected_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.recommended_option_projected_metrics.RecommendedOptionProjectedMetrics"
    ]
    """<p>An array of objects that describes projected metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEC2RecommendationProjectedMetricsResponse) -> dict:
    out: dict = {}
    if "recommended_option_projected_metrics" in value:
        import aws_sdk_compute_optimizer.types.recommended_option_projected_metrics

        out["recommendedOptionProjectedMetrics"] = (
            aws_sdk_compute_optimizer.types.recommended_option_projected_metrics.serialize_aws_json_1_0(
                value["recommended_option_projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetEC2RecommendationProjectedMetricsResponse:
    out: GetEC2RecommendationProjectedMetricsResponse = {}  # type: ignore[typeddict-item]
    if "recommendedOptionProjectedMetrics" in data:
        import aws_sdk_compute_optimizer.types.recommended_option_projected_metrics

        out["recommended_option_projected_metrics"] = (
            aws_sdk_compute_optimizer.types.recommended_option_projected_metrics.deserialize_aws_json_1_0(
                data["recommendedOptionProjectedMetrics"]
            )
        )
    return out
