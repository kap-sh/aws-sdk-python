"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeBasedForecastProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.periods_backward
    import aws_sdk_quicksight.types.periods_forward
    import aws_sdk_quicksight.types.prediction_interval
    import aws_sdk_quicksight.types.seasonality


class TimeBasedForecastProperties(TypedDict):
    periods_forward: NotRequired[
        "aws_sdk_quicksight.types.periods_forward.PeriodsForward"
    ]
    """<p>The periods forward setup of a forecast computation.</p>"""
    periods_backward: NotRequired[
        "aws_sdk_quicksight.types.periods_backward.PeriodsBackward"
    ]
    """<p>The periods backward setup of a forecast computation.</p>"""
    upper_boundary: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The upper boundary setup of a forecast computation.</p>"""
    lower_boundary: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The lower boundary setup of a forecast computation.</p>"""
    prediction_interval: NotRequired[
        "aws_sdk_quicksight.types.prediction_interval.PredictionInterval"
    ]
    """<p>The prediction interval setup of a forecast computation.</p>"""
    seasonality: NotRequired["aws_sdk_quicksight.types.seasonality.Seasonality"]
    """<p>The seasonality setup of a forecast computation. Choose one of the following options:</p> <ul> <li> <p> <code>NULL</code>: The input is set to <code>NULL</code>.</p> </li> <li> <p> <code>NON_NULL</code>: The input is set to a custom value.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeBasedForecastProperties) -> dict:
    out: dict = {}
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
        out["Seasonality"] = value["seasonality"]
    return out


def deserialize_json(data: dict) -> TimeBasedForecastProperties:
    out: TimeBasedForecastProperties = {}  # type: ignore[typeddict-item]
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
        out["seasonality"] = data["Seasonality"]
    return out
