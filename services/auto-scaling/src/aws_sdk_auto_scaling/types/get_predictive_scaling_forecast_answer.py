"""Generated from Smithy shape ``com.amazonaws.autoscaling#GetPredictiveScalingForecastAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.capacity_forecast
    import aws_sdk_auto_scaling.types.load_forecasts
    import aws_sdk_auto_scaling.types.timestamp_type


class GetPredictiveScalingForecastAnswer(TypedDict, closed=True):
    load_forecast: NotRequired[
        "aws_sdk_auto_scaling.types.load_forecasts.LoadForecasts"
    ]
    """<p>The load forecast.</p>"""
    capacity_forecast: NotRequired[
        "aws_sdk_auto_scaling.types.capacity_forecast.CapacityForecast"
    ]
    """<p>The capacity forecast.</p>"""
    update_time: NotRequired["aws_sdk_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The time the forecast was made.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPredictiveScalingForecastAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_forecast" in value:
        import aws_sdk_auto_scaling.types.load_forecasts

        aws_sdk_auto_scaling.types.load_forecasts.serialize_query(
            value["load_forecast"], pairs, f"{prefix}.LoadForecast"
        )
    if "capacity_forecast" in value:
        import aws_sdk_auto_scaling.types.capacity_forecast

        aws_sdk_auto_scaling.types.capacity_forecast.serialize_query(
            value["capacity_forecast"], pairs, f"{prefix}.CapacityForecast"
        )
    if "update_time" in value:
        import aws_sdk_auto_scaling.types.timestamp_type

        aws_sdk_auto_scaling.types.timestamp_type.serialize_query(
            value["update_time"], pairs, f"{prefix}.UpdateTime"
        )


def deserialize_query(el: Element) -> GetPredictiveScalingForecastAnswer:
    out: GetPredictiveScalingForecastAnswer = {}  # type: ignore[typeddict-item]
    child_load_forecast = el.find("LoadForecast")
    if child_load_forecast is not None:
        import aws_sdk_auto_scaling.types.load_forecasts

        out["load_forecast"] = (
            aws_sdk_auto_scaling.types.load_forecasts.deserialize_query(
                child_load_forecast
            )
        )
    child_capacity_forecast = el.find("CapacityForecast")
    if child_capacity_forecast is not None:
        import aws_sdk_auto_scaling.types.capacity_forecast

        out["capacity_forecast"] = (
            aws_sdk_auto_scaling.types.capacity_forecast.deserialize_query(
                child_capacity_forecast
            )
        )
    child_update_time = el.find("UpdateTime")
    if child_update_time is not None:
        import aws_sdk_auto_scaling.types.timestamp_type

        out["update_time"] = (
            aws_sdk_auto_scaling.types.timestamp_type.deserialize_query(
                child_update_time
            )
        )
    return out
