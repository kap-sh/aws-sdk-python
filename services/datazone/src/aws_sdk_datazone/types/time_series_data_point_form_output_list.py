"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointFormOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.time_series_data_point_form_output

TimeSeriesDataPointFormOutputList: TypeAlias = list[
    "aws_sdk_datazone.types.time_series_data_point_form_output.TimeSeriesDataPointFormOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointFormOutputList) -> list:
    import aws_sdk_datazone.types.time_series_data_point_form_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.time_series_data_point_form_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TimeSeriesDataPointFormOutputList:
    import aws_sdk_datazone.types.time_series_data_point_form_output

    out: TimeSeriesDataPointFormOutputList = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.time_series_data_point_form_output.deserialize_json(
                item
            )
        )
    return out
