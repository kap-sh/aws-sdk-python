"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.event_list
    import aws_sdk_memorydb.types.string


class DescribeEventsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    events: NotRequired["aws_sdk_memorydb.types.event_list.EventList"]
    """<p>A list of events. Each element in the list contains detailed information about one event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import aws_sdk_memorydb.types.event_list

        out["Events"] = aws_sdk_memorydb.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Events" in data:
        import aws_sdk_memorydb.types.event_list

        out["events"] = aws_sdk_memorydb.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out
