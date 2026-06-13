"""Generated from Smithy shape ``com.amazonaws.datazone#ListTimeSeriesDataPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list


class ListTimeSeriesDataPointsOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The results of the ListTimeSeriesDataPoints action. </p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesDataPointsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["items"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTimeSeriesDataPointsOutput:
    out: ListTimeSeriesDataPointsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["items"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
