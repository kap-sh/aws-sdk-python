"""Generated from Smithy shape ``com.amazonaws.notifications#ListEventRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rules
    import aws_sdk_notifications.types.next_token


class ListEventRulesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    event_rules: "aws_sdk_notifications.types.event_rules.EventRules"
    """<p>A list of <code>EventRules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_notifications.types.event_rules

    out["eventRules"] = aws_sdk_notifications.types.event_rules.serialize_json(
        value["event_rules"]
    )
    return out


def deserialize_json(data: dict) -> ListEventRulesResponse:
    out: ListEventRulesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "eventRules" in data:
        import aws_sdk_notifications.types.event_rules

        out["event_rules"] = aws_sdk_notifications.types.event_rules.deserialize_json(
            data["eventRules"]
        )
    else:
        raise DeserializationError("ListEventRulesResponse.event_rules required")
    return out
