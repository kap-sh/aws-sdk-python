"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListArchivesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive_name
    import aws_sdk_eventbridge.types.archive_state
    import aws_sdk_eventbridge.types.event_bus_arn
    import aws_sdk_eventbridge.types.limit_max100
    import aws_sdk_eventbridge.types.next_token


class ListArchivesRequest(TypedDict):
    name_prefix: NotRequired["aws_sdk_eventbridge.types.archive_name.ArchiveName"]
    """<p>A name prefix to filter the archives returned. Only archives with name that match the prefix are returned.</p>"""
    event_source_arn: NotRequired["aws_sdk_eventbridge.types.event_bus_arn.EventBusArn"]
    """<p>The ARN of the event source associated with the archive.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.archive_state.ArchiveState"]
    """<p>The state of the archive.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["aws_sdk_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArchivesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "state" in value:
        import aws_sdk_eventbridge.types.archive_state

        out["State"] = aws_sdk_eventbridge.types.archive_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArchivesRequest:
    out: ListArchivesRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "State" in data:
        import aws_sdk_eventbridge.types.archive_state

        out["state"] = aws_sdk_eventbridge.types.archive_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
