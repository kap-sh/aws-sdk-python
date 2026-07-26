"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RequestBasedServiceLevelIndicatorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.request_based_service_level_indicator_metric_config
    import capo_application_signals.types.service_level_indicator_comparison_operator
    import capo_application_signals.types.service_level_indicator_metric_threshold


class RequestBasedServiceLevelIndicatorConfig(TypedDict, closed=True):
    request_based_sli_metric_config: "capo_application_signals.types.request_based_service_level_indicator_metric_config.RequestBasedServiceLevelIndicatorMetricConfig"
    """<p>Use this structure to specify the metric to be used for the SLO.</p>"""
    metric_threshold: NotRequired[
        "capo_application_signals.types.service_level_indicator_metric_threshold.ServiceLevelIndicatorMetricThreshold"
    ]
    """<p>The value that the SLI metric is compared to. This parameter is required if this SLO is tracking the <code>Latency</code> metric.</p>"""
    comparison_operator: NotRequired[
        "capo_application_signals.types.service_level_indicator_comparison_operator.ServiceLevelIndicatorComparisonOperator"
    ]
    """<p>The arithmetic operation to use when comparing the specified metric to the threshold. This parameter is required if this SLO is tracking the <code>Latency</code> metric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestBasedServiceLevelIndicatorConfig) -> dict:
    out: dict = {}
    import capo_application_signals.types.request_based_service_level_indicator_metric_config

    out["RequestBasedSliMetricConfig"] = (
        capo_application_signals.types.request_based_service_level_indicator_metric_config.serialize_json(
            value["request_based_sli_metric_config"]
        )
    )
    if "metric_threshold" in value:
        out["MetricThreshold"] = value["metric_threshold"]
    if "comparison_operator" in value:
        import capo_application_signals.types.service_level_indicator_comparison_operator

        out["ComparisonOperator"] = (
            capo_application_signals.types.service_level_indicator_comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> RequestBasedServiceLevelIndicatorConfig:
    out: RequestBasedServiceLevelIndicatorConfig = {}  # type: ignore[typeddict-item]
    if "RequestBasedSliMetricConfig" in data:
        import capo_application_signals.types.request_based_service_level_indicator_metric_config

        out["request_based_sli_metric_config"] = (
            capo_application_signals.types.request_based_service_level_indicator_metric_config.deserialize_json(
                data["RequestBasedSliMetricConfig"]
            )
        )
    else:
        raise DeserializationError(
            "RequestBasedServiceLevelIndicatorConfig.request_based_sli_metric_config required"
        )
    if "MetricThreshold" in data:
        out["metric_threshold"] = data["MetricThreshold"]
    if "ComparisonOperator" in data:
        import capo_application_signals.types.service_level_indicator_comparison_operator

        out["comparison_operator"] = (
            capo_application_signals.types.service_level_indicator_comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    return out
