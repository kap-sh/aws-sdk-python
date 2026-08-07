"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityForecast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.predictive_scaling_forecast_timestamps
    import capo_auto_scaling.types.predictive_scaling_forecast_values


class CapacityForecast(TypedDict, closed=True):
    timestamps: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_forecast_timestamps.PredictiveScalingForecastTimestamps"
    ]
    """<p>The timestamps for the data points, in UTC format.</p>"""
    values: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_forecast_values.PredictiveScalingForecastValues"
    ]
    """<p>The values of the data points.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityForecast, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timestamps" in value:
        import capo_auto_scaling.types.predictive_scaling_forecast_timestamps

        capo_auto_scaling.types.predictive_scaling_forecast_timestamps.serialize_query(
            value["timestamps"], pairs, f"{key_prefix}Timestamps"
        )
    if "values" in value:
        import capo_auto_scaling.types.predictive_scaling_forecast_values

        capo_auto_scaling.types.predictive_scaling_forecast_values.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> CapacityForecast:
    out: CapacityForecast = {}  # type: ignore[typeddict-item]
    child_timestamps = el.find("Timestamps")
    if child_timestamps is not None:
        import capo_auto_scaling.types.predictive_scaling_forecast_timestamps

        out["timestamps"] = (
            capo_auto_scaling.types.predictive_scaling_forecast_timestamps.deserialize_query(
                child_timestamps
            )
        )
    child_values = el.find("Values")
    if child_values is not None:
        import capo_auto_scaling.types.predictive_scaling_forecast_values

        out["values"] = (
            capo_auto_scaling.types.predictive_scaling_forecast_values.deserialize_query(
                child_values
            )
        )
    return out
