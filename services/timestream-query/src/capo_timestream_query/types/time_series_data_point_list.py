"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TimeSeriesDataPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.time_series_data_point

TimeSeriesDataPointList: TypeAlias = list[
    "capo_timestream_query.types.time_series_data_point.TimeSeriesDataPoint"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeSeriesDataPointList) -> list:
    import capo_timestream_query.types.time_series_data_point

    out: list = []
    for item in value:
        out.append(
            capo_timestream_query.types.time_series_data_point.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TimeSeriesDataPointList:
    import capo_timestream_query.types.time_series_data_point

    out: TimeSeriesDataPointList = []
    for item in data:
        out.append(
            capo_timestream_query.types.time_series_data_point.deserialize_aws_json_1_0(
                item
            )
        )
    return out
