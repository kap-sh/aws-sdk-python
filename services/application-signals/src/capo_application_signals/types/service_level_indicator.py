"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicator``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_indicator_comparison_operator
    import capo_application_signals.types.service_level_indicator_metric
    import capo_application_signals.types.service_level_indicator_metric_threshold


class ServiceLevelIndicator(TypedDict, closed=True):
    sli_metric: "capo_application_signals.types.service_level_indicator_metric.ServiceLevelIndicatorMetric"
    """<p>A structure that contains information about the metric that the SLO monitors. </p>"""
    metric_threshold: "capo_application_signals.types.service_level_indicator_metric_threshold.ServiceLevelIndicatorMetricThreshold"
    """<p>The value that the SLI metric is compared to.</p>"""
    comparison_operator: "capo_application_signals.types.service_level_indicator_comparison_operator.ServiceLevelIndicatorComparisonOperator"
    """<p>The arithmetic operation used when comparing the specified metric to the threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelIndicator) -> dict:
    out: dict = {}
    import capo_application_signals.types.service_level_indicator_metric

    out["SliMetric"] = (
        capo_application_signals.types.service_level_indicator_metric.serialize_json(
            value["sli_metric"]
        )
    )
    out["MetricThreshold"] = value["metric_threshold"]
    import capo_application_signals.types.service_level_indicator_comparison_operator

    out["ComparisonOperator"] = (
        capo_application_signals.types.service_level_indicator_comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceLevelIndicator:
    out: ServiceLevelIndicator = {}  # type: ignore[typeddict-item]
    if "SliMetric" in data:
        import capo_application_signals.types.service_level_indicator_metric

        out["sli_metric"] = (
            capo_application_signals.types.service_level_indicator_metric.deserialize_json(
                data["SliMetric"]
            )
        )
    else:
        raise DeserializationError("ServiceLevelIndicator.sli_metric required")
    if "MetricThreshold" in data:
        out["metric_threshold"] = data["MetricThreshold"]
    else:
        raise DeserializationError("ServiceLevelIndicator.metric_threshold required")
    if "ComparisonOperator" in data:
        import capo_application_signals.types.service_level_indicator_comparison_operator

        out["comparison_operator"] = (
            capo_application_signals.types.service_level_indicator_comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    else:
        raise DeserializationError("ServiceLevelIndicator.comparison_operator required")
    return out
