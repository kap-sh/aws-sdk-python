"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListReplaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive_arn
    import aws_sdk_eventbridge.types.limit_max100
    import aws_sdk_eventbridge.types.next_token
    import aws_sdk_eventbridge.types.replay_name
    import aws_sdk_eventbridge.types.replay_state


class ListReplaysRequest(TypedDict, closed=True):
    name_prefix: NotRequired["aws_sdk_eventbridge.types.replay_name.ReplayName"]
    """<p>A name prefix to filter the replays returned. Only replays with name that match the prefix are returned.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.replay_state.ReplayState"]
    """<p>The state of the replay.</p>"""
    event_source_arn: NotRequired["aws_sdk_eventbridge.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive from which the events are replayed.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["aws_sdk_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of replays to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReplaysRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "state" in value:
        import aws_sdk_eventbridge.types.replay_state

        out["State"] = aws_sdk_eventbridge.types.replay_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReplaysRequest:
    out: ListReplaysRequest = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "State" in data:
        import aws_sdk_eventbridge.types.replay_state

        out["state"] = aws_sdk_eventbridge.types.replay_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
