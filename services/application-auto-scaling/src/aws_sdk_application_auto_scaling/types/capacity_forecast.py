"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#CapacityForecast``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps
    import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values


class CapacityForecast(TypedDict, closed=True):
    timestamps: "aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps.PredictiveScalingForecastTimestamps"
    """<p> The timestamps for the data points, in UTC format. </p>"""
    values: "aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values.PredictiveScalingForecastValues"
    """<p> The values of the data points. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityForecast) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityForecast:
    out: CapacityForecast = {}  # type: ignore[typeddict-item]
    if "Timestamps" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps

        out["timestamps"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_timestamps.deserialize_aws_json_1_1(
                data["Timestamps"]
            )
        )
    else:
        raise DeserializationError("CapacityForecast.timestamps required")
    if "Values" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values

        out["values"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_forecast_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("CapacityForecast.values required")
    return out
