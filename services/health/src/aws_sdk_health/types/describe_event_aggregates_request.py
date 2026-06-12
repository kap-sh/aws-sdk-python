"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventAggregatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_health.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_health.types.event_aggregate_field
    import aws_sdk_health.types.event_filter
    import aws_sdk_health.types.max_results
    import aws_sdk_health.types.next_token


class DescribeEventAggregatesRequest(TypedDict):
    filter: NotRequired["aws_sdk_health.types.event_filter.EventFilter"]
    """<p>Values to narrow the results returned.</p>"""
    aggregate_field: "aws_sdk_health.types.event_aggregate_field.eventAggregateField"
    """<p>The only currently supported value is <code>eventTypeCategory</code>.</p>"""
    max_results: NotRequired["aws_sdk_health.types.max_results.maxResults"]
    """<p>The maximum number of items to return in one batch, between 10 and 100, inclusive.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventAggregatesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_health.types.event_filter

        out["filter"] = aws_sdk_health.types.event_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    import aws_sdk_health.types.event_aggregate_field

    out["aggregateField"] = (
        aws_sdk_health.types.event_aggregate_field.serialize_aws_json_1_1(
            value["aggregate_field"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventAggregatesRequest:
    out: DescribeEventAggregatesRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_health.types.event_filter

        out["filter"] = aws_sdk_health.types.event_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    if "aggregateField" in data:
        import aws_sdk_health.types.event_aggregate_field

        out["aggregate_field"] = (
            aws_sdk_health.types.event_aggregate_field.deserialize_aws_json_1_1(
                data["aggregateField"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeEventAggregatesRequest.aggregate_field required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
