"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.event_type_batch
    import aws_sdk_codestar_notifications.types.next_token


class ListEventTypesResult(TypedDict):
    event_types: NotRequired[
        "aws_sdk_codestar_notifications.types.event_type_batch.EventTypeBatch"
    ]
    """<p>Information about each event, including service name, resource type, event ID, and event name.</p>"""
    next_token: NotRequired["aws_sdk_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesResult) -> dict:
    out: dict = {}
    if "event_types" in value:
        import aws_sdk_codestar_notifications.types.event_type_batch

        out["EventTypes"] = (
            aws_sdk_codestar_notifications.types.event_type_batch.serialize_json(
                value["event_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventTypesResult:
    out: ListEventTypesResult = {}  # type: ignore[typeddict-item]
    if "EventTypes" in data:
        import aws_sdk_codestar_notifications.types.event_type_batch

        out["event_types"] = (
            aws_sdk_codestar_notifications.types.event_type_batch.deserialize_json(
                data["EventTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
