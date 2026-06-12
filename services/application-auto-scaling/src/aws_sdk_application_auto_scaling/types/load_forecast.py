"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#LoadForecast``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification


class LoadForecast(TypedDict):
    timestamps: "aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps.PredictiveScalingForecastTimestamps"
    """<p> The timestamps for the data points, in UTC format. </p>"""
    values: "aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values.PredictiveScalingForecastValues"
    """<p> The values of the data points. </p>"""
    metric_specification: "aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification.PredictiveScalingMetricSpecification"
    """<p> The metric specification for the load forecast. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadForecast) -> dict:
    out: dict = {}
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps

    out["Timestamps"] = (
        aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps.serialize_aws_json_1_1(
            value["timestamps"]
        )
    )
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values

    out["Values"] = (
        aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification

    out["MetricSpecification"] = (
        aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification.serialize_aws_json_1_1(
            value["metric_specification"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadForecast:
    out: LoadForecast = {}  # type: ignore[typeddict-item]
    if "Timestamps" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps

        out["timestamps"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps.deserialize_aws_json_1_1(
                data["Timestamps"]
            )
        )
    else:
        raise DeserializationError("LoadForecast.timestamps required")
    if "Values" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values

        out["values"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("LoadForecast.values required")
    if "MetricSpecification" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification

        out["metric_specification"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_metric_specification.deserialize_aws_json_1_1(
                data["MetricSpecification"]
            )
        )
    else:
        raise DeserializationError("LoadForecast.metric_specification required")
    return out
