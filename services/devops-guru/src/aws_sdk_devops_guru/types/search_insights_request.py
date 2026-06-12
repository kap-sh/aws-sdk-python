"""Generated from Smithy shape ``com.amazonaws.devopsguru#SearchInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_type
    import aws_sdk_devops_guru.types.search_insights_filters
    import aws_sdk_devops_guru.types.search_insights_max_results
    import aws_sdk_devops_guru.types.start_time_range
    import aws_sdk_devops_guru.types.uuid_next_token


class SearchInsightsRequest(TypedDict):
    start_time_range: "aws_sdk_devops_guru.types.start_time_range.StartTimeRange"
    """<p> The start of the time range passed in. Returned insights occurred after this time. </p>"""
    filters: NotRequired[
        "aws_sdk_devops_guru.types.search_insights_filters.SearchInsightsFilters"
    ]
    """<p> A <code>SearchInsightsFilters</code> object that is used to set the severity and status filters on your insight search. </p>"""
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.search_insights_max_results.SearchInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    type: "aws_sdk_devops_guru.types.insight_type.InsightType"
    """<p> The type of insights you are searching for (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchInsightsRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.start_time_range

    out["StartTimeRange"] = aws_sdk_devops_guru.types.start_time_range.serialize_json(
        value["start_time_range"]
    )
    if "filters" in value:
        import aws_sdk_devops_guru.types.search_insights_filters

        out["Filters"] = (
            aws_sdk_devops_guru.types.search_insights_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_devops_guru.types.insight_type

    out["Type"] = aws_sdk_devops_guru.types.insight_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SearchInsightsRequest:
    out: SearchInsightsRequest = {}  # type: ignore[typeddict-item]
    if "StartTimeRange" in data:
        import aws_sdk_devops_guru.types.start_time_range

        out["start_time_range"] = (
            aws_sdk_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    else:
        raise DeserializationError("SearchInsightsRequest.start_time_range required")
    if "Filters" in data:
        import aws_sdk_devops_guru.types.search_insights_filters

        out["filters"] = (
            aws_sdk_devops_guru.types.search_insights_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Type" in data:
        import aws_sdk_devops_guru.types.insight_type

        out["type"] = aws_sdk_devops_guru.types.insight_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("SearchInsightsRequest.type required")
    return out
