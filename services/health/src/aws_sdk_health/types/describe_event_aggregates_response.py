"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventAggregatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.event_aggregate_list
    import aws_sdk_health.types.next_token


class DescribeEventAggregatesResponse(TypedDict):
    event_aggregates: NotRequired[
        "aws_sdk_health.types.event_aggregate_list.EventAggregateList"
    ]
    """<p>The number of events in each category that meet the optional filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventAggregatesResponse) -> dict:
    out: dict = {}
    if "event_aggregates" in value:
        import aws_sdk_health.types.event_aggregate_list

        out["eventAggregates"] = (
            aws_sdk_health.types.event_aggregate_list.serialize_aws_json_1_1(
                value["event_aggregates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventAggregatesResponse:
    out: DescribeEventAggregatesResponse = {}  # type: ignore[typeddict-item]
    if "eventAggregates" in data:
        import aws_sdk_health.types.event_aggregate_list

        out["event_aggregates"] = (
            aws_sdk_health.types.event_aggregate_list.deserialize_aws_json_1_1(
                data["eventAggregates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
