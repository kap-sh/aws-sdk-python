"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateAlarmModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_capabilities
    import aws_sdk_iot_events.types.alarm_event_actions
    import aws_sdk_iot_events.types.alarm_model_description
    import aws_sdk_iot_events.types.alarm_model_name
    import aws_sdk_iot_events.types.alarm_notification
    import aws_sdk_iot_events.types.alarm_rule
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.severity


class UpdateAlarmModelRequest(TypedDict):
    alarm_model_name: "aws_sdk_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    alarm_model_description: NotRequired[
        "aws_sdk_iot_events.types.alarm_model_description.AlarmModelDescription"
    ]
    """<p>The description of the alarm model.</p>"""
    role_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    r"""<p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    severity: NotRequired["aws_sdk_iot_events.types.severity.Severity"]
    """<p>A non-negative integer that reflects the severity level of the alarm.</p>"""
    alarm_rule: "aws_sdk_iot_events.types.alarm_rule.AlarmRule"
    """<p>Defines when your alarm is invoked.</p>"""
    alarm_notification: NotRequired[
        "aws_sdk_iot_events.types.alarm_notification.AlarmNotification"
    ]
    """<p>Contains information about one or more notification actions.</p>"""
    alarm_event_actions: NotRequired[
        "aws_sdk_iot_events.types.alarm_event_actions.AlarmEventActions"
    ]
    """<p>Contains information about one or more alarm actions.</p>"""
    alarm_capabilities: NotRequired[
        "aws_sdk_iot_events.types.alarm_capabilities.AlarmCapabilities"
    ]
    """<p>Contains the configuration information of alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAlarmModelRequest) -> dict:
    out: dict = {}
    if "alarm_model_description" in value:
        out["alarmModelDescription"] = value["alarm_model_description"]
    out["roleArn"] = value["role_arn"]
    if "severity" in value:
        out["severity"] = value["severity"]
    import aws_sdk_iot_events.types.alarm_rule

    out["alarmRule"] = aws_sdk_iot_events.types.alarm_rule.serialize_json(
        value["alarm_rule"]
    )
    if "alarm_notification" in value:
        import aws_sdk_iot_events.types.alarm_notification

        out["alarmNotification"] = (
            aws_sdk_iot_events.types.alarm_notification.serialize_json(
                value["alarm_notification"]
            )
        )
    if "alarm_event_actions" in value:
        import aws_sdk_iot_events.types.alarm_event_actions

        out["alarmEventActions"] = (
            aws_sdk_iot_events.types.alarm_event_actions.serialize_json(
                value["alarm_event_actions"]
            )
        )
    if "alarm_capabilities" in value:
        import aws_sdk_iot_events.types.alarm_capabilities

        out["alarmCapabilities"] = (
            aws_sdk_iot_events.types.alarm_capabilities.serialize_json(
                value["alarm_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAlarmModelRequest:
    out: UpdateAlarmModelRequest = {}  # type: ignore[typeddict-item]
    if "alarmModelDescription" in data:
        out["alarm_model_description"] = data["alarmModelDescription"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateAlarmModelRequest.role_arn required")
    if "severity" in data:
        out["severity"] = data["severity"]
    if "alarmRule" in data:
        import aws_sdk_iot_events.types.alarm_rule

        out["alarm_rule"] = aws_sdk_iot_events.types.alarm_rule.deserialize_json(
            data["alarmRule"]
        )
    else:
        raise DeserializationError("UpdateAlarmModelRequest.alarm_rule required")
    if "alarmNotification" in data:
        import aws_sdk_iot_events.types.alarm_notification

        out["alarm_notification"] = (
            aws_sdk_iot_events.types.alarm_notification.deserialize_json(
                data["alarmNotification"]
            )
        )
    if "alarmEventActions" in data:
        import aws_sdk_iot_events.types.alarm_event_actions

        out["alarm_event_actions"] = (
            aws_sdk_iot_events.types.alarm_event_actions.deserialize_json(
                data["alarmEventActions"]
            )
        )
    if "alarmCapabilities" in data:
        import aws_sdk_iot_events.types.alarm_capabilities

        out["alarm_capabilities"] = (
            aws_sdk_iot_events.types.alarm_capabilities.deserialize_json(
                data["alarmCapabilities"]
            )
        )
    return out
