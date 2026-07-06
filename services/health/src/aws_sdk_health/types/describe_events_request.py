"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.event_filter
    import aws_sdk_health.types.locale
    import aws_sdk_health.types.max_results_lower_range
    import aws_sdk_health.types.next_token


class DescribeEventsRequest(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_health.types.event_filter.EventFilter"]
    """<p>Values to narrow the results returned.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""
    max_results: NotRequired[
        "aws_sdk_health.types.max_results_lower_range.maxResultsLowerRange"
    ]
    """<p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>"""
    locale: NotRequired["aws_sdk_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_health.types.event_filter

        out["filter"] = aws_sdk_health.types.event_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsRequest:
    out: DescribeEventsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_health.types.event_filter

        out["filter"] = aws_sdk_health.types.event_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
