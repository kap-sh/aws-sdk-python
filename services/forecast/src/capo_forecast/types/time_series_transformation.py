"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.action
    import capo_forecast.types.time_series_conditions


class TimeSeriesTransformation(TypedDict, closed=True):
    action: NotRequired["capo_forecast.types.action.Action"]
    """<p>An array of actions that define a time series and how it is transformed. These transformations create a new time series that is used for the what-if analysis.</p>"""
    time_series_conditions: NotRequired[
        "capo_forecast.types.time_series_conditions.TimeSeriesConditions"
    ]
    """<p>An array of conditions that define which members of the related time series are transformed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesTransformation) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_forecast.types.action

        out["Action"] = capo_forecast.types.action.serialize_aws_json_1_1(
            value["action"]
        )
    if "time_series_conditions" in value:
        import capo_forecast.types.time_series_conditions

        out["TimeSeriesConditions"] = (
            capo_forecast.types.time_series_conditions.serialize_aws_json_1_1(
                value["time_series_conditions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesTransformation:
    out: TimeSeriesTransformation = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_forecast.types.action

        out["action"] = capo_forecast.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "TimeSeriesConditions" in data:
        import capo_forecast.types.time_series_conditions

        out["time_series_conditions"] = (
            capo_forecast.types.time_series_conditions.deserialize_aws_json_1_1(
                data["TimeSeriesConditions"]
            )
        )
    return out
