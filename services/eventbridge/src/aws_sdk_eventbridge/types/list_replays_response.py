"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListReplaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.next_token
    import aws_sdk_eventbridge.types.replay_list


class ListReplaysResponse(TypedDict, closed=True):
    replays: NotRequired["aws_sdk_eventbridge.types.replay_list.ReplayList"]
    """<p>An array of <code>Replay</code> objects that contain information about the replay.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReplaysResponse) -> dict:
    out: dict = {}
    if "replays" in value:
        import aws_sdk_eventbridge.types.replay_list

        out["Replays"] = aws_sdk_eventbridge.types.replay_list.serialize_aws_json_1_1(
            value["replays"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReplaysResponse:
    out: ListReplaysResponse = {}  # type: ignore[typeddict-item]
    if "Replays" in data:
        import aws_sdk_eventbridge.types.replay_list

        out["replays"] = aws_sdk_eventbridge.types.replay_list.deserialize_aws_json_1_1(
            data["Replays"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
