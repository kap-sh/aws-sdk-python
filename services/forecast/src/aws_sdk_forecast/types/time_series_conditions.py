"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.time_series_condition

TimeSeriesConditions: TypeAlias = list[
    "aws_sdk_forecast.types.time_series_condition.TimeSeriesCondition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesConditions) -> list:
    import aws_sdk_forecast.types.time_series_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.time_series_condition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TimeSeriesConditions:
    import aws_sdk_forecast.types.time_series_condition

    out: TimeSeriesConditions = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.time_series_condition.deserialize_aws_json_1_1(item)
        )
    return out
