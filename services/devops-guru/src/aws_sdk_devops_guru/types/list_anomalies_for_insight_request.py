"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomaliesForInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.aws_account_id
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_filters
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_max_results
    import aws_sdk_devops_guru.types.start_time_range
    import aws_sdk_devops_guru.types.uuid_next_token


class ListAnomaliesForInsightRequest(TypedDict, closed=True):
    insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId"
    """<p> The ID of the insight. The returned anomalies belong to this insight. </p>"""
    start_time_range: NotRequired[
        "aws_sdk_devops_guru.types.start_time_range.StartTimeRange"
    ]
    """<p> A time range used to specify when the requested anomalies started. All returned anomalies started during this time range. </p>"""
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.list_anomalies_for_insight_max_results.ListAnomaliesForInsightMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    account_id: NotRequired["aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account. </p>"""
    filters: NotRequired[
        "aws_sdk_devops_guru.types.list_anomalies_for_insight_filters.ListAnomaliesForInsightFilters"
    ]
    """<p> Specifies one or more service names that are used to list anomalies. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomaliesForInsightRequest) -> dict:
    out: dict = {}
    if "start_time_range" in value:
        import aws_sdk_devops_guru.types.start_time_range

        out["StartTimeRange"] = (
            aws_sdk_devops_guru.types.start_time_range.serialize_json(
                value["start_time_range"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "filters" in value:
        import aws_sdk_devops_guru.types.list_anomalies_for_insight_filters

        out["Filters"] = (
            aws_sdk_devops_guru.types.list_anomalies_for_insight_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAnomaliesForInsightRequest:
    out: ListAnomaliesForInsightRequest = {}  # type: ignore[typeddict-item]
    if "StartTimeRange" in data:
        import aws_sdk_devops_guru.types.start_time_range

        out["start_time_range"] = (
            aws_sdk_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Filters" in data:
        import aws_sdk_devops_guru.types.list_anomalies_for_insight_filters

        out["filters"] = (
            aws_sdk_devops_guru.types.list_anomalies_for_insight_filters.deserialize_json(
                data["Filters"]
            )
        )
    return out
