"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListReplaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_arn
    import capo_eventbridge.types.limit_max100
    import capo_eventbridge.types.next_token
    import capo_eventbridge.types.replay_name
    import capo_eventbridge.types.replay_state


class ListReplaysRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_eventbridge.types.replay_name.ReplayName"]
    """<p>A name prefix to filter the replays returned. Only replays with name that match the prefix are returned.</p>"""
    state: NotRequired["capo_eventbridge.types.replay_state.ReplayState"]
    """<p>The state of the replay.</p>"""
    event_source_arn: NotRequired["capo_eventbridge.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive from which the events are replayed.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>The token returned by a previous call, which you can use to retrieve the next set of results.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""
    limit: NotRequired["capo_eventbridge.types.limit_max100.LimitMax100"]
    """<p>The maximum number of replays to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReplaysRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "state" in value:
        import capo_eventbridge.types.replay_state

        out["State"] = capo_eventbridge.types.replay_state.serialize_aws_json_1_1(
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
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("State") is not None:
        import capo_eventbridge.types.replay_state

        out["state"] = capo_eventbridge.types.replay_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
