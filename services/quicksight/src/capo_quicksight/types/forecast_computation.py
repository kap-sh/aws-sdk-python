"""Generated from Smithy shape ``com.amazonaws.quicksight#ForecastComputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.double
    import capo_quicksight.types.forecast_computation_custom_seasonality_value
    import capo_quicksight.types.forecast_computation_seasonality
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.periods_backward
    import capo_quicksight.types.periods_forward
    import capo_quicksight.types.prediction_interval
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string


class ForecastComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    periods_forward: NotRequired["capo_quicksight.types.periods_forward.PeriodsForward"]
    """<p>The periods forward setup of a forecast computation.</p>"""
    periods_backward: NotRequired[
        "capo_quicksight.types.periods_backward.PeriodsBackward"
    ]
    """<p>The periods backward setup of a forecast computation.</p>"""
    upper_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The upper boundary setup of a forecast computation.</p>"""
    lower_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The lower boundary setup of a forecast computation.</p>"""
    prediction_interval: NotRequired[
        "capo_quicksight.types.prediction_interval.PredictionInterval"
    ]
    """<p>The prediction interval setup of a forecast computation.</p>"""
    seasonality: NotRequired[
        "capo_quicksight.types.forecast_computation_seasonality.ForecastComputationSeasonality"
    ]
    """<p>The seasonality setup of a forecast computation. Choose one of the following options:</p> <ul> <li> <p> <code>AUTOMATIC</code> </p> </li> <li> <p> <code>CUSTOM</code>: Checks the custom seasonality value.</p> </li> </ul>"""
    custom_seasonality_value: NotRequired[
        "capo_quicksight.types.forecast_computation_custom_seasonality_value.ForecastComputationCustomSeasonalityValue"
    ]
    """<p>The custom seasonality value setup of a forecast computation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import capo_quicksight.types.dimension_field

        out["Time"] = capo_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["Value"] = capo_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "periods_forward" in value:
        out["PeriodsForward"] = value["periods_forward"]
    if "periods_backward" in value:
        out["PeriodsBackward"] = value["periods_backward"]
    if "upper_boundary" in value:
        out["UpperBoundary"] = value["upper_boundary"]
    if "lower_boundary" in value:
        out["LowerBoundary"] = value["lower_boundary"]
    if "prediction_interval" in value:
        out["PredictionInterval"] = value["prediction_interval"]
    if "seasonality" in value:
        import capo_quicksight.types.forecast_computation_seasonality

        out["Seasonality"] = (
            capo_quicksight.types.forecast_computation_seasonality.serialize_json(
                value["seasonality"]
            )
        )
    if "custom_seasonality_value" in value:
        out["CustomSeasonalityValue"] = value["custom_seasonality_value"]
    return out


def deserialize_json(data: dict) -> ForecastComputation:
    out: ForecastComputation = {}  # type: ignore[typeddict-item]
    if "ComputationId" in data:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("ForecastComputation.computation_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Time" in data:
        import capo_quicksight.types.dimension_field

        out["time"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
    if "Value" in data:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if "PeriodsForward" in data:
        out["periods_forward"] = data["PeriodsForward"]
    if "PeriodsBackward" in data:
        out["periods_backward"] = data["PeriodsBackward"]
    if "UpperBoundary" in data:
        out["upper_boundary"] = data["UpperBoundary"]
    if "LowerBoundary" in data:
        out["lower_boundary"] = data["LowerBoundary"]
    if "PredictionInterval" in data:
        out["prediction_interval"] = data["PredictionInterval"]
    if "Seasonality" in data:
        import capo_quicksight.types.forecast_computation_seasonality

        out["seasonality"] = (
            capo_quicksight.types.forecast_computation_seasonality.deserialize_json(
                data["Seasonality"]
            )
        )
    if "CustomSeasonalityValue" in data:
        out["custom_seasonality_value"] = data["CustomSeasonalityValue"]
    return out
