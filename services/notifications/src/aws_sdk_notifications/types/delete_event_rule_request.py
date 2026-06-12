"""Generated from Smithy shape ``com.amazonaws.notifications#DeleteEventRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_arn

class DeleteEventRuleRequest(TypedDict):
    arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventRuleRequest:
    out: DeleteEventRuleRequest = {}  # type: ignore[typeddict-item]
    return out