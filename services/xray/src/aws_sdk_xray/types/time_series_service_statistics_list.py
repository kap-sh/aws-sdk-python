"""Generated from Smithy shape ``com.amazonaws.xray#TimeSeriesServiceStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.time_series_service_statistics

TimeSeriesServiceStatisticsList: TypeAlias = list[
    "aws_sdk_xray.types.time_series_service_statistics.TimeSeriesServiceStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesServiceStatisticsList) -> list:
    import aws_sdk_xray.types.time_series_service_statistics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_xray.types.time_series_service_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TimeSeriesServiceStatisticsList:
    import aws_sdk_xray.types.time_series_service_statistics

    out: TimeSeriesServiceStatisticsList = []
    for item in data:
        out.append(
            aws_sdk_xray.types.time_series_service_statistics.deserialize_json(item)
        )
    return out
