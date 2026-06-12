"""Generated from Smithy shape ``com.amazonaws.notifications#GetEventRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_arn

class GetEventRuleRequest(TypedDict):
    arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to return.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetEventRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventRuleRequest:
    out: GetEventRuleRequest = {}  # type: ignore[typeddict-item]
    return out