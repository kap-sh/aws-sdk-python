"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListEventActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_event_action_entry
    import aws_sdk_dataexchange.types.next_token


class ListEventActionsResponse(TypedDict, closed=True):
    event_actions: NotRequired[
        "aws_sdk_dataexchange.types.list_of_event_action_entry.ListOfEventActionEntry"
    ]
    """<p>The event action objects listed by the request.</p>"""
    next_token: NotRequired["aws_sdk_dataexchange.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventActionsResponse) -> dict:
    out: dict = {}
    if "event_actions" in value:
        import aws_sdk_dataexchange.types.list_of_event_action_entry

        out["EventActions"] = (
            aws_sdk_dataexchange.types.list_of_event_action_entry.serialize_json(
                value["event_actions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventActionsResponse:
    out: ListEventActionsResponse = {}  # type: ignore[typeddict-item]
    if "EventActions" in data:
        import aws_sdk_dataexchange.types.list_of_event_action_entry

        out["event_actions"] = (
            aws_sdk_dataexchange.types.list_of_event_action_entry.deserialize_json(
                data["EventActions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
