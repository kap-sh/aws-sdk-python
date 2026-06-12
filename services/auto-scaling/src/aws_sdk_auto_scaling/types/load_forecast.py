"""Generated from Smithy shape ``com.amazonaws.autoscaling#LoadForecast``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps
    import aws_sdk_auto_scaling.types.predictive_scaling_forecast_values
    import aws_sdk_auto_scaling.types.predictive_scaling_metric_specification


class LoadForecast(TypedDict):
    timestamps: NotRequired[
        "aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps.PredictiveScalingForecastTimestamps"
    ]
    """<p>The timestamps for the data points, in UTC format.</p>"""
    values: NotRequired[
        "aws_sdk_auto_scaling.types.predictive_scaling_forecast_values.PredictiveScalingForecastValues"
    ]
    """<p>The values of the data points.</p>"""
    metric_specification: NotRequired[
        "aws_sdk_auto_scaling.types.predictive_scaling_metric_specification.PredictiveScalingMetricSpecification"
    ]
    """<p>The metric specification for the load forecast.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadForecast, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "timestamps" in value:
        import aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps

        aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps.serialize_query(
            value["timestamps"], pairs, f"{prefix}.Timestamps"
        )
    if "values" in value:
        import aws_sdk_auto_scaling.types.predictive_scaling_forecast_values

        aws_sdk_auto_scaling.types.predictive_scaling_forecast_values.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )
    if "metric_specification" in value:
        import aws_sdk_auto_scaling.types.predictive_scaling_metric_specification

        aws_sdk_auto_scaling.types.predictive_scaling_metric_specification.serialize_query(
            value["metric_specification"], pairs, f"{prefix}.MetricSpecification"
        )


def deserialize_query(el: Element) -> LoadForecast:
    out: LoadForecast = {}  # type: ignore[typeddict-item]
    child_timestamps = el.find("Timestamps")
    if child_timestamps is not None:
        import aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps

        out["timestamps"] = (
            aws_sdk_auto_scaling.types.predictive_scaling_forecast_timestamps.deserialize_query(
                child_timestamps
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_auto_scaling.types.predictive_scaling_forecast_values

        out["values"] = (
            aws_sdk_auto_scaling.types.predictive_scaling_forecast_values.deserialize_query(
                child_values
            )
        )
    child_metric_specification = el.find("MetricSpecification")
    if child_metric_specification is not None:
        import aws_sdk_auto_scaling.types.predictive_scaling_metric_specification

        out["metric_specification"] = (
            aws_sdk_auto_scaling.types.predictive_scaling_metric_specification.deserialize_query(
                child_metric_specification
            )
        )
    return out
