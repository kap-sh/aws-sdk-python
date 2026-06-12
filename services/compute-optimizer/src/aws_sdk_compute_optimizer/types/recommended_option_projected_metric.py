"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.projected_metrics
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.recommended_instance_type


class RecommendedOptionProjectedMetric(TypedDict):
    recommended_instance_type: NotRequired[
        "aws_sdk_compute_optimizer.types.recommended_instance_type.RecommendedInstanceType"
    ]
    """<p>The recommended instance type.</p>"""
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p>The rank of the recommendation option projected metric.</p> <p>The top recommendation option is ranked as <code>1</code>.</p> <p>The projected metric rank correlates to the recommendation option rank. For example, the projected metric ranked as <code>1</code> is related to the recommendation option that is also ranked as <code>1</code> in the same response.</p>"""
    projected_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.projected_metrics.ProjectedMetrics"
    ]
    """<p>An array of objects that describe a projected utilization metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import aws_sdk_compute_optimizer.types.projected_metrics

        out["projectedMetrics"] = (
            aws_sdk_compute_optimizer.types.projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedOptionProjectedMetric:
    out: RecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if "recommendedInstanceType" in data:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if "rank" in data:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if "projectedMetrics" in data:
        import aws_sdk_compute_optimizer.types.projected_metrics

        out["projected_metrics"] = (
            aws_sdk_compute_optimizer.types.projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out
