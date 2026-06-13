"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateEventRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_arn
    import aws_sdk_notifications.types.event_rule_event_pattern
    import aws_sdk_notifications.types.regions


class UpdateEventRuleRequest(TypedDict):
    arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>"""
    event_pattern: NotRequired[
        "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
    ]
    """<p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>"""
    regions: NotRequired["aws_sdk_notifications.types.regions.Regions"]
    """<p>A list of Amazon Web Services Regions that sends events to this <code>EventRule</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventRuleRequest) -> dict:
    out: dict = {}
    if "event_pattern" in value:
        out["eventPattern"] = value["event_pattern"]
    if "regions" in value:
        import aws_sdk_notifications.types.regions

        out["regions"] = aws_sdk_notifications.types.regions.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEventRuleRequest:
    out: UpdateEventRuleRequest = {}  # type: ignore[typeddict-item]
    if "eventPattern" in data:
        out["event_pattern"] = data["eventPattern"]
    if "regions" in data:
        import aws_sdk_notifications.types.regions

        out["regions"] = aws_sdk_notifications.types.regions.deserialize_json(
            data["regions"]
        )
    return out
