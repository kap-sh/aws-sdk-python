"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#GetPredictiveScalingForecastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.capacity_forecast
    import capo_application_auto_scaling.types.load_forecasts
    import capo_application_auto_scaling.types.timestamp_type


class GetPredictiveScalingForecastResponse(TypedDict, closed=True):
    load_forecast: NotRequired[
        "capo_application_auto_scaling.types.load_forecasts.LoadForecasts"
    ]
    """<p> The load forecast. </p>"""
    capacity_forecast: NotRequired[
        "capo_application_auto_scaling.types.capacity_forecast.CapacityForecast"
    ]
    """<p> The capacity forecast. </p>"""
    update_time: NotRequired[
        "capo_application_auto_scaling.types.timestamp_type.TimestampType"
    ]
    """<p> The time the forecast was made. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPredictiveScalingForecastResponse) -> dict:
    out: dict = {}
    if "load_forecast" in value:
        import capo_application_auto_scaling.types.load_forecasts

        out["LoadForecast"] = (
            capo_application_auto_scaling.types.load_forecasts.serialize_aws_json_1_1(
                value["load_forecast"]
            )
        )
    if "capacity_forecast" in value:
        import capo_application_auto_scaling.types.capacity_forecast

        out["CapacityForecast"] = (
            capo_application_auto_scaling.types.capacity_forecast.serialize_aws_json_1_1(
                value["capacity_forecast"]
            )
        )
    if "update_time" in value:
        import capo_application_auto_scaling.types.timestamp_type

        out["UpdateTime"] = (
            capo_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
                value["update_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPredictiveScalingForecastResponse:
    out: GetPredictiveScalingForecastResponse = {}  # type: ignore[typeddict-item]
    if "LoadForecast" in data:
        import capo_application_auto_scaling.types.load_forecasts

        out["load_forecast"] = (
            capo_application_auto_scaling.types.load_forecasts.deserialize_aws_json_1_1(
                data["LoadForecast"]
            )
        )
    if "CapacityForecast" in data:
        import capo_application_auto_scaling.types.capacity_forecast

        out["capacity_forecast"] = (
            capo_application_auto_scaling.types.capacity_forecast.deserialize_aws_json_1_1(
                data["CapacityForecast"]
            )
        )
    if "UpdateTime" in data:
        import capo_application_auto_scaling.types.timestamp_type

        out["update_time"] = (
            capo_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["UpdateTime"]
            )
        )
    return out
