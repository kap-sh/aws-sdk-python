"""Generated from Smithy shape ``com.amazonaws.macie2#GetUsageStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__list_of_usage_statistics_filter
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.time_range
    import aws_sdk_macie2.types.usage_statistics_sort_by


class GetUsageStatisticsRequest(TypedDict):
    filter_by: NotRequired[
        "aws_sdk_macie2.types.__list_of_usage_statistics_filter.__listOfUsageStatisticsFilter"
    ]
    """<p>An array of objects, one for each condition to use to filter the query results. If you specify more than one condition, Amazon Macie uses an AND operator to join the conditions.</p>"""
    max_results: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_by: NotRequired[
        "aws_sdk_macie2.types.usage_statistics_sort_by.UsageStatisticsSortBy"
    ]
    """<p>The criteria to use to sort the query results.</p>"""
    time_range: NotRequired["aws_sdk_macie2.types.time_range.TimeRange"]
    """<p>The inclusive time period to query usage data for. Valid values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days. If you don't specify a value, Amazon Macie provides usage data for the preceding 30 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_by" in value:
        import aws_sdk_macie2.types.__list_of_usage_statistics_filter

        out["filterBy"] = (
            aws_sdk_macie2.types.__list_of_usage_statistics_filter.serialize_json(
                value["filter_by"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_by" in value:
        import aws_sdk_macie2.types.usage_statistics_sort_by

        out["sortBy"] = aws_sdk_macie2.types.usage_statistics_sort_by.serialize_json(
            value["sort_by"]
        )
    if "time_range" in value:
        import aws_sdk_macie2.types.time_range

        out["timeRange"] = aws_sdk_macie2.types.time_range.serialize_json(
            value["time_range"]
        )
    return out


def deserialize_json(data: dict) -> GetUsageStatisticsRequest:
    out: GetUsageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "filterBy" in data:
        import aws_sdk_macie2.types.__list_of_usage_statistics_filter

        out["filter_by"] = (
            aws_sdk_macie2.types.__list_of_usage_statistics_filter.deserialize_json(
                data["filterBy"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortBy" in data:
        import aws_sdk_macie2.types.usage_statistics_sort_by

        out["sort_by"] = aws_sdk_macie2.types.usage_statistics_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "timeRange" in data:
        import aws_sdk_macie2.types.time_range

        out["time_range"] = aws_sdk_macie2.types.time_range.deserialize_json(
            data["timeRange"]
        )
    return out
