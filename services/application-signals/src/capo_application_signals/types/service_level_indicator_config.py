"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelIndicatorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_indicator_comparison_operator
    import capo_application_signals.types.service_level_indicator_metric_config
    import capo_application_signals.types.service_level_indicator_metric_threshold


class ServiceLevelIndicatorConfig(TypedDict, closed=True):
    sli_metric_config: "capo_application_signals.types.service_level_indicator_metric_config.ServiceLevelIndicatorMetricConfig"
    """<p>Use this structure to specify the metric to be used for the SLO.</p>"""
    metric_threshold: "capo_application_signals.types.service_level_indicator_metric_threshold.ServiceLevelIndicatorMetricThreshold"
    """<p>This parameter is used only when a request-based SLO tracks the <code>Latency</code> metric. Specify the threshold value that the observed <code>Latency</code> metric values are to be compared to.</p> <p>This is not required if <code>CreateRecommendedSlo</code> is set to <code>true</code>.</p>"""
    comparison_operator: "capo_application_signals.types.service_level_indicator_comparison_operator.ServiceLevelIndicatorComparisonOperator"
    """<p>The arithmetic operation to use when comparing the specified metric to the threshold.</p> <p>This is not required if <code>CreateRecommendedSlo</code> is set to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelIndicatorConfig) -> dict:
    out: dict = {}
    import capo_application_signals.types.service_level_indicator_metric_config

    out["SliMetricConfig"] = (
        capo_application_signals.types.service_level_indicator_metric_config.serialize_json(
            value["sli_metric_config"]
        )
    )
    out["MetricThreshold"] = value.get("metric_threshold", 0)
    import capo_application_signals.types.service_level_indicator_comparison_operator

    out["ComparisonOperator"] = (
        capo_application_signals.types.service_level_indicator_comparison_operator.serialize_json(
            value.get("comparison_operator", "LessThan")
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceLevelIndicatorConfig:
    out: ServiceLevelIndicatorConfig = {}  # type: ignore[typeddict-item]
    if "SliMetricConfig" in data:
        import capo_application_signals.types.service_level_indicator_metric_config

        out["sli_metric_config"] = (
            capo_application_signals.types.service_level_indicator_metric_config.deserialize_json(
                data["SliMetricConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceLevelIndicatorConfig.sli_metric_config required"
        )
    if "MetricThreshold" in data:
        out["metric_threshold"] = data["MetricThreshold"]
    else:
        out["metric_threshold"] = 0
    if "ComparisonOperator" in data:
        import capo_application_signals.types.service_level_indicator_comparison_operator

        out["comparison_operator"] = (
            capo_application_signals.types.service_level_indicator_comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    else:
        out["comparison_operator"] = "LessThan"
    return out
