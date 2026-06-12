"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.event_list
    import aws_sdk_health.types.next_token


class DescribeEventsResponse(TypedDict):
    events: NotRequired["aws_sdk_health.types.event_list.EventList"]
    """<p>The events that match the specified filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_health.types.event_list

        out["events"] = aws_sdk_health.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_health.types.event_list

        out["events"] = aws_sdk_health.types.event_list.deserialize_aws_json_1_1(
            data["events"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
