"""Generated from Smithy shape ``com.amazonaws.notifications#CreateEventRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.event_rule_event_pattern
    import aws_sdk_notifications.types.event_type
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.regions
    import aws_sdk_notifications.types.source


class CreateEventRuleRequest(TypedDict):
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> associated with this <code>EventRule</code>.</p>"""
    source: "aws_sdk_notifications.types.source.Source"
    """<p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    event_type: "aws_sdk_notifications.types.event_type.EventType"
    """<p>The event type to match.</p> <p>Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    event_pattern: NotRequired[
        "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
    ]
    """<p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>"""
    regions: "aws_sdk_notifications.types.regions.Regions"
    """<p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventRuleRequest) -> dict:
    out: dict = {}
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    out["source"] = value["source"]
    out["eventType"] = value["event_type"]
    if "event_pattern" in value:
        out["eventPattern"] = value["event_pattern"]
    import aws_sdk_notifications.types.regions

    out["regions"] = aws_sdk_notifications.types.regions.serialize_json(
        value["regions"]
    )
    return out


def deserialize_json(data: dict) -> CreateEventRuleRequest:
    out: CreateEventRuleRequest = {}  # type: ignore[typeddict-item]
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateEventRuleRequest.notification_configuration_arn required"
        )
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("CreateEventRuleRequest.source required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("CreateEventRuleRequest.event_type required")
    if "eventPattern" in data:
        out["event_pattern"] = data["eventPattern"]
    if "regions" in data:
        import aws_sdk_notifications.types.regions

        out["regions"] = aws_sdk_notifications.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("CreateEventRuleRequest.regions required")
    return out
