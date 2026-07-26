"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.time_series_condition

TimeSeriesConditions: TypeAlias = list[
    "capo_forecast.types.time_series_condition.TimeSeriesCondition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesConditions) -> list:
    import capo_forecast.types.time_series_condition

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.time_series_condition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TimeSeriesConditions:
    import capo_forecast.types.time_series_condition

    out: TimeSeriesConditions = []
    for item in data:
        out.append(
            capo_forecast.types.time_series_condition.deserialize_aws_json_1_1(item)
        )
    return out
