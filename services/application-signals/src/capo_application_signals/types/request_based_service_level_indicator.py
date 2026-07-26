"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RequestBasedServiceLevelIndicator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.request_based_service_level_indicator_metric
    import capo_application_signals.types.service_level_indicator_comparison_operator
    import capo_application_signals.types.service_level_indicator_metric_threshold


class RequestBasedServiceLevelIndicator(TypedDict, closed=True):
    request_based_sli_metric: "capo_application_signals.types.request_based_service_level_indicator_metric.RequestBasedServiceLevelIndicatorMetric"
    """<p>A structure that contains information about the metric that the SLO monitors. </p>"""
    metric_threshold: NotRequired[
        "capo_application_signals.types.service_level_indicator_metric_threshold.ServiceLevelIndicatorMetricThreshold"
    ]
    """<p>This value is the threshold that the observed metric values of the SLI metric are compared to.</p>"""
    comparison_operator: NotRequired[
        "capo_application_signals.types.service_level_indicator_comparison_operator.ServiceLevelIndicatorComparisonOperator"
    ]
    """<p>The arithmetic operation used when comparing the specified metric to the threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestBasedServiceLevelIndicator) -> dict:
    out: dict = {}
    import capo_application_signals.types.request_based_service_level_indicator_metric

    out["RequestBasedSliMetric"] = (
        capo_application_signals.types.request_based_service_level_indicator_metric.serialize_json(
            value["request_based_sli_metric"]
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


def deserialize_json(data: dict) -> RequestBasedServiceLevelIndicator:
    out: RequestBasedServiceLevelIndicator = {}  # type: ignore[typeddict-item]
    if "RequestBasedSliMetric" in data:
        import capo_application_signals.types.request_based_service_level_indicator_metric

        out["request_based_sli_metric"] = (
            capo_application_signals.types.request_based_service_level_indicator_metric.deserialize_json(
                data["RequestBasedSliMetric"]
            )
        )
    else:
        raise DeserializationError(
            "RequestBasedServiceLevelIndicator.request_based_sli_metric required"
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
