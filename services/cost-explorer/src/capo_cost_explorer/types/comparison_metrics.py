"""Generated from Smithy shape ``com.amazonaws.costexplorer#ComparisonMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.comparison_metric_value
    import capo_cost_explorer.types.metric_name

ComparisonMetrics: TypeAlias = dict[
    "capo_cost_explorer.types.metric_name.MetricName",
    "capo_cost_explorer.types.comparison_metric_value.ComparisonMetricValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ComparisonMetrics) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cost_explorer.types.comparison_metric_value

        out[key] = (
            capo_cost_explorer.types.comparison_metric_value.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComparisonMetrics:
    out: ComparisonMetrics = {}
    for key, value in data.items():
        import capo_cost_explorer.types.comparison_metric_value

        out[key] = (
            capo_cost_explorer.types.comparison_metric_value.deserialize_aws_json_1_1(
                value
            )
        )
    return out
