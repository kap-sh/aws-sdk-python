"""Generated from Smithy shape ``com.amazonaws.forecastquery#TimeSeries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecastquery.types.data_point

TimeSeries: TypeAlias = list["aws_sdk_forecastquery.types.data_point.DataPoint"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeries) -> list:
    import aws_sdk_forecastquery.types.data_point

    out: list = []
    for item in value:
        out.append(aws_sdk_forecastquery.types.data_point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TimeSeries:
    import aws_sdk_forecastquery.types.data_point

    out: TimeSeries = []
    for item in data:
        out.append(
            aws_sdk_forecastquery.types.data_point.deserialize_aws_json_1_1(item)
        )
    return out
