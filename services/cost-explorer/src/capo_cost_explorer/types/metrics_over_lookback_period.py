"""Generated from Smithy shape ``com.amazonaws.costexplorer#MetricsOverLookbackPeriod``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.recommendation_detail_hourly_metrics

MetricsOverLookbackPeriod: TypeAlias = list[
    "capo_cost_explorer.types.recommendation_detail_hourly_metrics.RecommendationDetailHourlyMetrics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsOverLookbackPeriod) -> list:
    import capo_cost_explorer.types.recommendation_detail_hourly_metrics

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.recommendation_detail_hourly_metrics.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricsOverLookbackPeriod:
    import capo_cost_explorer.types.recommendation_detail_hourly_metrics

    out: MetricsOverLookbackPeriod = []
    for item in data:
        out.append(
            capo_cost_explorer.types.recommendation_detail_hourly_metrics.deserialize_aws_json_1_1(
                item
            )
        )
    return out
