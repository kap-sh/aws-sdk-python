"""Generated from Smithy shape ``com.amazonaws.iotevents#TransitionEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.actions
    import aws_sdk_iot_events.types.condition
    import aws_sdk_iot_events.types.event_name
    import aws_sdk_iot_events.types.state_name


class TransitionEvent(TypedDict):
    event_name: "aws_sdk_iot_events.types.event_name.EventName"
    """<p>The name of the transition event.</p>"""
    condition: "aws_sdk_iot_events.types.condition.Condition"
    """<p>Required. A Boolean expression that when TRUE causes the actions to be performed and the <code>nextState</code> to be entered.</p>"""
    actions: NotRequired["aws_sdk_iot_events.types.actions.Actions"]
    """<p>The actions to be performed.</p>"""
    next_state: "aws_sdk_iot_events.types.state_name.StateName"
    """<p>The next state to enter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitionEvent) -> dict:
    out: dict = {}
    out["eventName"] = value["event_name"]
    out["condition"] = value["condition"]
    if "actions" in value:
        import aws_sdk_iot_events.types.actions

        out["actions"] = aws_sdk_iot_events.types.actions.serialize_json(
            value["actions"]
        )
    out["nextState"] = value["next_state"]
    return out


def deserialize_json(data: dict) -> TransitionEvent:
    out: TransitionEvent = {}  # type: ignore[typeddict-item]
    if "eventName" in data:
        out["event_name"] = data["eventName"]
    else:
        raise DeserializationError("TransitionEvent.event_name required")
    if "condition" in data:
        out["condition"] = data["condition"]
    else:
        raise DeserializationError("TransitionEvent.condition required")
    if "actions" in data:
        import aws_sdk_iot_events.types.actions

        out["actions"] = aws_sdk_iot_events.types.actions.deserialize_json(
            data["actions"]
        )
    if "nextState" in data:
        out["next_state"] = data["nextState"]
    else:
        raise DeserializationError("TransitionEvent.next_state required")
    return out
