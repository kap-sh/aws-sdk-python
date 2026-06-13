"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointSummaryFormOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output

TimeSeriesDataPointSummaryFormOutputList: TypeAlias = list[
    "aws_sdk_datazone.types.time_series_data_point_summary_form_output.TimeSeriesDataPointSummaryFormOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointSummaryFormOutputList) -> list:
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.time_series_data_point_summary_form_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TimeSeriesDataPointSummaryFormOutputList:
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output

    out: TimeSeriesDataPointSummaryFormOutputList = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.time_series_data_point_summary_form_output.deserialize_json(
                item
            )
        )
    return out
