"""Generated from Smithy shape ``com.amazonaws.macie2#GetUsageStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer
    import capo_macie2.types.__list_of_usage_statistics_filter
    import capo_macie2.types.__string
    import capo_macie2.types.time_range
    import capo_macie2.types.usage_statistics_sort_by


class GetUsageStatisticsRequest(TypedDict, closed=True):
    filter_by: NotRequired[
        "capo_macie2.types.__list_of_usage_statistics_filter.__listOfUsageStatisticsFilter"
    ]
    """<p>An array of objects, one for each condition to use to filter the query results. If you specify more than one condition, Amazon Macie uses an AND operator to join the conditions.</p>"""
    max_results: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The maximum number of items to include in each page of the response.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""
    sort_by: NotRequired[
        "capo_macie2.types.usage_statistics_sort_by.UsageStatisticsSortBy"
    ]
    """<p>The criteria to use to sort the query results.</p>"""
    time_range: NotRequired["capo_macie2.types.time_range.TimeRange"]
    """<p>The inclusive time period to query usage data for. Valid values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days. If you don't specify a value, Amazon Macie provides usage data for the preceding 30 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_by" in value:
        import capo_macie2.types.__list_of_usage_statistics_filter

        out["filterBy"] = (
            capo_macie2.types.__list_of_usage_statistics_filter.serialize_json(
                value["filter_by"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_macie2.types.usage_statistics_sort_by

        out["sortBy"] = capo_macie2.types.usage_statistics_sort_by.serialize_json(
            value["sort_by"]
        )
    if "time_range" in value:
        import capo_macie2.types.time_range

        out["timeRange"] = capo_macie2.types.time_range.serialize_json(
            value["time_range"]
        )
    return out


def deserialize_json(data: dict) -> GetUsageStatisticsRequest:
    out: GetUsageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "filterBy" in data:
        import capo_macie2.types.__list_of_usage_statistics_filter

        out["filter_by"] = (
            capo_macie2.types.__list_of_usage_statistics_filter.deserialize_json(
                data["filterBy"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortBy" in data:
        import capo_macie2.types.usage_statistics_sort_by

        out["sort_by"] = capo_macie2.types.usage_statistics_sort_by.deserialize_json(
            data["sortBy"]
        )
    if "timeRange" in data:
        import capo_macie2.types.time_range

        out["time_range"] = capo_macie2.types.time_range.deserialize_json(
            data["timeRange"]
        )
    return out
