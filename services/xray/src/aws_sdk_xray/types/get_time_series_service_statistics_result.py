"""Generated from Smithy shape ``com.amazonaws.xray#GetTimeSeriesServiceStatisticsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.boolean
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.time_series_service_statistics_list


class GetTimeSeriesServiceStatisticsResult(TypedDict, closed=True):
    time_series_service_statistics: NotRequired[
        "aws_sdk_xray.types.time_series_service_statistics_list.TimeSeriesServiceStatisticsList"
    ]
    """<p>The collection of statistics.</p>"""
    contains_old_group_versions: "aws_sdk_xray.types.boolean.Boolean"
    """<p>A flag indicating whether or not a group's filter expression has been consistent, or if a returned aggregation might show statistics from an older version of the group's filter expression.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeSeriesServiceStatisticsResult) -> dict:
    out: dict = {}
    if "time_series_service_statistics" in value:
        import aws_sdk_xray.types.time_series_service_statistics_list

        out["TimeSeriesServiceStatistics"] = (
            aws_sdk_xray.types.time_series_service_statistics_list.serialize_json(
                value["time_series_service_statistics"]
            )
        )
    out["ContainsOldGroupVersions"] = value.get("contains_old_group_versions", False)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTimeSeriesServiceStatisticsResult:
    out: GetTimeSeriesServiceStatisticsResult = {}  # type: ignore[typeddict-item]
    if "TimeSeriesServiceStatistics" in data:
        import aws_sdk_xray.types.time_series_service_statistics_list

        out["time_series_service_statistics"] = (
            aws_sdk_xray.types.time_series_service_statistics_list.deserialize_json(
                data["TimeSeriesServiceStatistics"]
            )
        )
    if "ContainsOldGroupVersions" in data:
        out["contains_old_group_versions"] = data["ContainsOldGroupVersions"]
    else:
        out["contains_old_group_versions"] = False
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
