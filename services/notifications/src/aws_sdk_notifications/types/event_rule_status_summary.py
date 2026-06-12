"""Generated from Smithy shape ``com.amazonaws.notifications#EventRuleStatusSummary``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_notifications.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_status
    import aws_sdk_notifications.types.event_rule_status_reason

class EventRuleStatusSummary(TypedDict):
    status: "aws_sdk_notifications.types.event_rule_status.EventRuleStatus"
    """<p>The status of the <code>EventRule</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>The <code>EventRule</code> can process events.</p> </li> </ul> </li> <li> <p> <code>INACTIVE</code> </p> <ul> <li> <p>The <code>EventRule</code> may be unable to process events.</p> </li> </ul> </li> <li> <p> <code>CREATING</code> </p> <ul> <li> <p>The <code>EventRule</code> is being created.</p> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> <li> <p> <code>UPDATING</code> </p> <ul> <li> <p>The <code>EventRule</code> is being updated.</p> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> <li> <p> <code>DELETING</code> </p> <ul> <li> <p>The <code>EventRule</code> is being deleted.</p> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> </ul> </li> </ul>"""
    reason: "aws_sdk_notifications.types.event_rule_status_reason.EventRuleStatusReason"
    """<p>A human-readable reason for <code>EventRuleStatus</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EventRuleStatusSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> EventRuleStatusSummary:
    out: EventRuleStatusSummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EventRuleStatusSummary.status required")
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("EventRuleStatusSummary.reason required")
    return out