"""Generated from Smithy shape ``com.amazonaws.opensearch#ListScheduledActionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.scheduled_actions_list


class ListScheduledActionsResponse(TypedDict):
    scheduled_actions: NotRequired[
        "aws_sdk_opensearch.types.scheduled_actions_list.ScheduledActionsList"
    ]
    """<p>A list of actions that are scheduled for the domain.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduledActionsResponse) -> dict:
    out: dict = {}
    if "scheduled_actions" in value:
        import aws_sdk_opensearch.types.scheduled_actions_list

        out["ScheduledActions"] = (
            aws_sdk_opensearch.types.scheduled_actions_list.serialize_json(
                value["scheduled_actions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScheduledActionsResponse:
    out: ListScheduledActionsResponse = {}  # type: ignore[typeddict-item]
    if "ScheduledActions" in data:
        import aws_sdk_opensearch.types.scheduled_actions_list

        out["scheduled_actions"] = (
            aws_sdk_opensearch.types.scheduled_actions_list.deserialize_json(
                data["ScheduledActions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
