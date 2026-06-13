"""Generated from Smithy shape ``com.amazonaws.notifications#GetEventRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.event_rule_arn
    import aws_sdk_notifications.types.event_rule_event_pattern
    import aws_sdk_notifications.types.event_type
    import aws_sdk_notifications.types.managed_rule_arns
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.regions
    import aws_sdk_notifications.types.source
    import aws_sdk_notifications.types.status_summary_by_region


class GetEventRuleResponse(TypedDict):
    arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The ARN of the resource.</p>"""
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of a <code>NotificationConfiguration</code>.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The date when the <code>EventRule</code> was created.</p>"""
    source: "aws_sdk_notifications.types.source.Source"
    """<p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    event_type: "aws_sdk_notifications.types.event_type.EventType"
    """<p>The event type to match.</p> <p>Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    event_pattern: (
        "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
    )
    """<p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>"""
    regions: "aws_sdk_notifications.types.regions.Regions"
    """<p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>"""
    managed_rules: "aws_sdk_notifications.types.managed_rule_arns.ManagedRuleArns"
    """<p>A list of managed rules from EventBridge that are associated with this <code>EventRule</code>.</p> <note> <p>These are created by User Notifications within your account so this <code>EventRule</code> functions.</p> </note>"""
    status_summary_by_region: (
        "aws_sdk_notifications.types.status_summary_by_region.StatusSummaryByRegion"
    )
    """<p>A list of an <code>EventRule</code>'s status by Region. Regions are mapped to <code>EventRuleStatusSummary</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventRuleResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    out["source"] = value["source"]
    out["eventType"] = value["event_type"]
    out["eventPattern"] = value["event_pattern"]
    import aws_sdk_notifications.types.regions

    out["regions"] = aws_sdk_notifications.types.regions.serialize_json(
        value["regions"]
    )
    import aws_sdk_notifications.types.managed_rule_arns

    out["managedRules"] = aws_sdk_notifications.types.managed_rule_arns.serialize_json(
        value["managed_rules"]
    )
    import aws_sdk_notifications.types.status_summary_by_region

    out["statusSummaryByRegion"] = (
        aws_sdk_notifications.types.status_summary_by_region.serialize_json(
            value["status_summary_by_region"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetEventRuleResponse:
    out: GetEventRuleResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetEventRuleResponse.arn required")
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "GetEventRuleResponse.notification_configuration_arn required"
        )
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("GetEventRuleResponse.creation_time required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("GetEventRuleResponse.source required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("GetEventRuleResponse.event_type required")
    if "eventPattern" in data:
        out["event_pattern"] = data["eventPattern"]
    else:
        raise DeserializationError("GetEventRuleResponse.event_pattern required")
    if "regions" in data:
        import aws_sdk_notifications.types.regions

        out["regions"] = aws_sdk_notifications.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("GetEventRuleResponse.regions required")
    if "managedRules" in data:
        import aws_sdk_notifications.types.managed_rule_arns

        out["managed_rules"] = (
            aws_sdk_notifications.types.managed_rule_arns.deserialize_json(
                data["managedRules"]
            )
        )
    else:
        raise DeserializationError("GetEventRuleResponse.managed_rules required")
    if "statusSummaryByRegion" in data:
        import aws_sdk_notifications.types.status_summary_by_region

        out["status_summary_by_region"] = (
            aws_sdk_notifications.types.status_summary_by_region.deserialize_json(
                data["statusSummaryByRegion"]
            )
        )
    else:
        raise DeserializationError(
            "GetEventRuleResponse.status_summary_by_region required"
        )
    return out
