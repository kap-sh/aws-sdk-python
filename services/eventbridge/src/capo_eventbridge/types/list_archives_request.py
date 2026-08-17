"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListArchivesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_name
    import capo_eventbridge.types.archive_state
    import capo_eventbridge.types.event_bus_arn
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token


class ListArchivesRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_eventbridge.types.archive_name.ArchiveName"]
    """<p>A name prefix to filter the archives returned. Only archives with name that match the prefix are returned.</p>"""
    event_source_arn: NotRequired["capo_eventbridge.types.event_bus_arn.EventBusArn"]
    """<p>The ARN of the event source associated with the archive.</p>"""
    state: NotRequired["capo_eventbridge.types.archive_state.ArchiveState"]
    """<p>The state of the archive.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArchivesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "state" in value:
        import capo_eventbridge.types.archive_state

        out["State"] = capo_eventbridge.types.archive_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArchivesRequest:
    out: ListArchivesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("State") is not None:
        import capo_eventbridge.types.archive_state

        out["state"] = capo_eventbridge.types.archive_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
