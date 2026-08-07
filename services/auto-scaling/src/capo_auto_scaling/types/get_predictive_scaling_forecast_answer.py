"""Generated from Smithy shape ``com.amazonaws.autoscaling#GetPredictiveScalingForecastAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.capacity_forecast
    import capo_auto_scaling.types.load_forecasts
    import capo_auto_scaling.types.timestamp_type


class GetPredictiveScalingForecastAnswer(TypedDict, closed=True):
    load_forecast: NotRequired["capo_auto_scaling.types.load_forecasts.LoadForecasts"]
    """<p>The load forecast.</p>"""
    capacity_forecast: NotRequired[
        "capo_auto_scaling.types.capacity_forecast.CapacityForecast"
    ]
    """<p>The capacity forecast.</p>"""
    update_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The time the forecast was made.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPredictiveScalingForecastAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_forecast" in value:
        import capo_auto_scaling.types.load_forecasts

        capo_auto_scaling.types.load_forecasts.serialize_query(
            value["load_forecast"], pairs, f"{key_prefix}LoadForecast"
        )
    if "capacity_forecast" in value:
        import capo_auto_scaling.types.capacity_forecast

        capo_auto_scaling.types.capacity_forecast.serialize_query(
            value["capacity_forecast"], pairs, f"{key_prefix}CapacityForecast"
        )
    if "update_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["update_time"], pairs, f"{key_prefix}UpdateTime"
        )


def deserialize_query(el: Element) -> GetPredictiveScalingForecastAnswer:
    out: GetPredictiveScalingForecastAnswer = {}  # type: ignore[typeddict-item]
    child_load_forecast = el.find("LoadForecast")
    if child_load_forecast is not None:
        import capo_auto_scaling.types.load_forecasts

        out["load_forecast"] = capo_auto_scaling.types.load_forecasts.deserialize_query(
            child_load_forecast
        )
    child_capacity_forecast = el.find("CapacityForecast")
    if child_capacity_forecast is not None:
        import capo_auto_scaling.types.capacity_forecast

        out["capacity_forecast"] = (
            capo_auto_scaling.types.capacity_forecast.deserialize_query(
                child_capacity_forecast
            )
        )
    child_update_time = el.find("UpdateTime")
    if child_update_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["update_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_update_time
        )
    return out
